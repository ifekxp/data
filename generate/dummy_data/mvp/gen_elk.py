from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker

# Reference: https://pypi.org/project/Faker/

fake=Faker()

es = Elasticsearch()
es = Elasticsearch({'127.0.0.1'})

actions = [
  {
    "_index": "users",
    "_type": "doc",
    "_source": {
	  "name": fake.name(),
	  "street": fake.street_address(), 
	  "city": fake.city(),
	  "zip":fake.zipcode()}
  }
  for x in range(998)
]

res = helpers.bulk(es, actions)
