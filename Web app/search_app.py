from flask import Flask, request
from markupsafe import escape
from flask import render_template
from elasticsearch import Elasticsearch
import math

"""Change your elastic password here"""
ELASTIC_PASSWORD = "boss4237"

es = Elasticsearch("https://localhost:9200", http_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    page_size = 10
    keyword = request.args.get('keyword')
    if request.args.get('page'):
        page_no = int(request.args.get('page'))
    else:
        page_no = 1

    body = {
    'size': page_size,
    'from': page_size * (page_no - 1),
    'query': {
    'multi_match': {
        'query': keyword,
        'fields': ['title^3', 'plot_summary^2', 'genres^1', 'themes^1'],
        'fuzziness': 'AUTO'
        }
    }
}

    res = es.search(index='anime', body=body)
    hits = [
        {
            'animeID': doc['_source']['animeID'],
            'title': doc['_source']['title'],
            'plot_summary': doc['_source']['plot_summary'],
            'image_url': doc['_source']['image_url'],
            'genres': doc['_source']['genres'],
        }
        for doc in res['hits']['hits']
    ]
    page_total = math.ceil(res['hits']['total']['value']/page_size)
    return render_template('search.html',keyword=keyword, hits=hits, page_no=page_no, page_total=page_total)