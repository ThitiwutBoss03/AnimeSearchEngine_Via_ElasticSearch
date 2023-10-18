from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "your_password"

es = Elasticsearch("https://localhost:9200", http_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)

# Define the index name to be deleted
index_name = "anime"

# Check if the index exists before deleting
if es.indices.exists(index=index_name):
    # Delete the index
    es.indices.delete(index=index_name)
    print(f"Index '{index_name}' has been deleted.")
else:
    print(f"Index '{index_name}' does not exist.")

# Close the Elasticsearch client connection (optional)
es.transport.close()
