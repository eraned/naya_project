import requests
import json
import os
from datetime import datetime,date,timedelta
import time
import pandas as pd

# airflow
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from google.cloud import bigquery


class OpenExchangeToKafka(BaseOperator):
    @apply_defaults
    def __init__(self
                 , token
                 , url
                 , destination_dataset_table
                 ,destination_dataset
                 , write_disposition
                 , schema_update_options
                 ,create_disposition
                 , *args, **kwargs):
        super(OpenExchangeToKafka, self).__init__(*args, **kwargs)
        self.token = token
        self.url = url
        self.destination_dataset_table = destination_dataset_table
        self.destination_dataset = destination_dataset
        self.write_disposition = write_disposition
        self.schema_update_options = schema_update_options
        self.create_disposition = create_disposition

    def openexchange_api_call(self,http_method, url_suffix, data=None, params=None, json=None, headers=None):
        url = f'{self.url}{url_suffix}'
        if http_method == 'GET':
            response = requests.get(url, data=data, params=params, json=json, headers=headers)
        else:
            return False
        if response.status_code in (200, 201, 204):
            return response.json()
        else:
            print(f'Error status code: {response.status_code}')
            print(f'Error: {response.content}')
            exit(1)


    def delete_before_insert(self,date_to_delete,destination_dataset,bq_client):
        query = f"""delete from `guesty-data.{destination_dataset}.currency_converter` where currency_rate_date = '{date_to_delete}'"""
        res_df = bq_client.query_bigquery(query)
        print(f"delete succeeded : {res_df.empty}")


    def currency_rates_backfill(self,start_date,end_date,params,bq_client,job_config):
        delta = timedelta(days=1)
        while start_date <= end_date:
            url_suffix = f'historical/{start_date.strftime("%Y-%m-%d")}.json'
            start_date += delta
            response = self.openexchange_api_call('GET',url_suffix=url_suffix,params=params)
            currency_rate_date = datetime.fromtimestamp(response.get('timestamp')).date().strftime("%Y-%m-%d")
            base_currency = response.get('base')
            curr_rates_df = pd.DataFrame(list(response.get('rates').items()), columns=['currency', 'value'])
            curr_rates_df["currency_rate_date"] = currency_rate_date
            curr_rates_df["base_currency"] = base_currency
            bq_client.load_to_bigquery(df=curr_rates_df, bq_destination=self.destination_dataset_table,job_config=job_config)
        print("backfill process finished....")


    def execute(self, context):
        sm = SecretManagerClient()
        OE_TOKEN = sm.get_secret_val(self.token)
        params = {'app_id':  OE_TOKEN}
        bq_client = BigQuery()
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = self.write_disposition
        job_config.schema_update_options = self.schema_update_options
        job_config.create_disposition = self.create_disposition
        #### backfill area for past dates ####
        # start_date = date(2020, 12, 31)
        # end_date = date(2021, 7, 18)
        # self.currency_rates_backfill(start_date,end_date,params,bq_client,job_config)
        ######################################
        url_suffix = 'latest.json'
        response = self.openexchange_api_call('GET',url_suffix=url_suffix,params=params)
        currency_rate_date_str = datetime.fromtimestamp(response.get('timestamp')).date().strftime("%Y-%m-%d")
        base_currency = response.get('base')
        curr_rates_df = pd.DataFrame(list(response.get('rates').items()), columns=['currency', 'value'])
        curr_rates_df["currency_rate_date"] = currency_rate_date_str
        curr_rates_df["base_currency"] = base_currency
        query = f"""select currency_rate_date from `guesty-data.{self.destination_dataset}.currency_converter` where currency_rate_date = '{currency_rate_date_str}' group by 1"""
        res_df = bq_client.query_bigquery(query)
        if not res_df.empty:
            self.delete_before_insert(currency_rate_date_str,self.destination_dataset,bq_client)
            print("delete before insert stage completed succecfuly")
        bq_client.load_to_bigquery(df=curr_rates_df, bq_destination=self.destination_dataset_table,job_config=job_config)
