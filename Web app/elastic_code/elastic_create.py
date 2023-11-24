from elasticsearch import Elasticsearch
import ndjson

ELASTIC_PASSWORD = "boss4237"

es = Elasticsearch("https://localhost:9200", http_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)

# Define the index name
index_name = "anime"

try:
    # Create the empty index
    es.indices.create(index=index_name, ignore=400)  # Ignore 400 status if the index already exists
    print(f"Index {index_name} has been created")

    # Define the path to the NDJSON file
    ndjson_file_path = r"C:\Users\Thitiwut\Documents\GitHub\AnimeSearchEngine_Via_ElasticSearch\Web app\elastic_code\anime_data5.json"

    # Read the NDJSON file and automatically detect the mapping
    documents = []
    with open(ndjson_file_path, 'r') as ndjson_file:
        for doc in ndjson.load(ndjson_file):
            documents.append(doc)

    # Add the documents to the index using the Bulk API
    request_body = []
    for doc in documents:
        request_body.append({
            "index": {
                "_index": index_name
            }
        })
        request_body.append(doc)

    es.bulk(index=index_name, body=request_body)
    print(f"{len(documents)} documents have been added to the index.")

except Exception as e:
    print("\nERROR:", e)

# Close the Elasticsearch client connection (optional)
es.transport.close()
