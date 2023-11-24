from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "boss4237"

es = Elasticsearch("https://localhost:9200", http_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)

# Define the index and query
index_name = "anime"
page_size = 10
keyword = "detective conan"

body = {
        'size': page_size,
        'query': {
        'multi_match': {
            'query': keyword,
            'fields': ['title^3', 'plot_summary^2', 'genres^1', 'themes^1'],
            'fuzziness': 'AUTO'
        }
    }
    }

# Perform the search
result = es.search(index=index_name, body=body)

# Process the search results
for hit in result['hits']['hits']:
    print(f"Score: {hit['_score']}, Source: {hit['_source']}")

# Close the Elasticsearch client connection (optional)
es.transport.close()
