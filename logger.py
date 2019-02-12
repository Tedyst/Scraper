import elasticsearch
import json
es = elasticsearch.Elasticsearch([{'host': '172.28.0.5', 'port': 9200}])


def connect_elasticsearch():
    if es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')


def log(data):
    json = {
        "timp": data[0],
        "pret": data[1],
        "name": data[2],
        "url": data[3],
        "source": data[4]
    }
    searchJson = {
        "query": {
            "match_phrase": {
                "url": data[3]
            }
        },
        "sort": {
            "timp": "desc"
        },
        "size": 1
    }
    result = es.search(index="scraper", doc_type='preturi', body=searchJson)
    try:
        pretVechi = int(result['hits']['hits'][0]['_source']['pret'])
        if pretVechi != data[1]:
            es.index(index='scraper', doc_type='preturi', body=json)
    except:
        es.index(index='scraper', doc_type='preturi', body=json)


def create_index():
    index_name = 'scraper'
    created = False
    settings = {
        "mappings": {
            "preturi": {
                "dynamic": "strict",
                "properties": {
                    "timp": {
                        "type": "date",
                        "format": "epoch_second"
                    },
                    "pret": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "source": {
                        "type": "text"
                    }
                }
            }
        }
    }

    try:
        if not es.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es.indices.create(
                index=index_name, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def search(index_name, search):
    res = es.search(index=index_name, body=search)
    print(res)


connect_elasticsearch()
create_index()
