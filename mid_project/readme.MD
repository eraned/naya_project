# Instructions

1. Create Twitter App with developer account on twitter 

**http://apps.twitter.com**

2. Bring up a local ElasticSearch + Kibana docker environment

```
$ docker-compose up
```

3. Run the python program, which will stream live tweets (according to the filter assigned) and store the relevant data inside ElasticSerch. For example, the following command will filter streaming tweets with the keyword "israel" and store them in the index_israel index (which will be created if doesn't already exist).
```
python main.py --index-name index_israel --filter israel
```