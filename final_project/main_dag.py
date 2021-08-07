# airflow
from airflow import DAG
from airflow import utils
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.exceptions import AirflowException

# plugins
from airflow.plugins.operators.openexchange_operator import OpenExchangeToKafka

# other
import os

DAGS_FOLDER = os.getenv("DAGS_FOLDER")
DAG_SCHEDULER = '@daily'
EMAIL_LIST = ['eran.edri@guesty.com']
REDIS_DEST = ''
ETL_NAME = 'main_dag'
YESTERDAY = utils.dates.days_ago(1)

# ---------------------------------------------------------------------------- #
# Tasks environments :
# ---------------------------------------------------------------------------- #

tasks_items = [
    {
        'task_name': 'openexchange_task',
        'destination_dataset' : REDIS_DEST,
        'write_disposition': 'WRITE_APPEND',
        'token': "OPENEXCHANGE",
        'url': "https://openexchangerates.org/api/",
        'schema_update_options': ('ALLOW_FIELD_ADDITION', 'ALLOW_FIELD_RELAXATION'),
        'create_disposition': 'CREATE_IF_NEEDED',
        "operator_type": "openexchange"
    }
]

# ---------------------------------------------------------------------------- #
# Create dag
# ---------------------------------------------------------------------------- #
default_args = {
    'start_date': YESTERDAY,
    'email': EMAIL_LIST,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
}

dag = DAG(ETL_NAME,
          default_args=default_args,
          schedule_interval=DAG_SCHEDULER,
          catchup=False,
          concurrency=6)

with dag:
    # dummy tasks
    kick_off_dag = DummyOperator(task_id='kick_off_dag')
    end_of_dag = DummyOperator(task_id='end_dag')
    prev_task = kick_off_dag

    #### tasks items ####
    for task in tasks_items:
        operator_type = task.get('operator_type')

        # task operator
        if operator_type == 'openexchange':
            oe_task = OpenExchangeToKafka(
                task_id=task.get('task_name')
                , token=task.get('token')
                ,url = task.get('url')
                ,destination_dataset = task.get('destination_dataset')
                , destination_dataset_table=task.get('destination_dataset_table')
                , write_disposition=task.get('write_disposition')
                , schema_update_options=task.get('schema_update_options')
                ,create_disposition = task.get('create_disposition')
            )

                # oe_task.execute({})

            ##### task flow ####
            prev_task >> oe_task
            prev_task = oe_task

        else:
            raise AirflowException

    prev_task >> end_of_dag


print("eran_test")