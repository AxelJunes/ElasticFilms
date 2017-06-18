# Libraries
import pandas as pd
import json
from elasticsearch import Elasticsearch
from flask import Flask, render_template, request

app = Flask(__name__)

#---------------------------------------------------------------------
# Get data frame with data from movies
df = pd.read_csv('western.csv', sep=';')
es = Elasticsearch()
es.indices.create(index="western", ignore=400)
# Index all the movies in ElasticSearch
for i in range(1, len(df.index)):
    es.index(index='western', doc_type='movie', body={
        'id': i,
        'title': df.loc[i]['title'],
        'plot': df.loc[i]['plot']
    })
#---------------------------------------------------------------------

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":
        query = request.form["query"]
        # Query with ElasticSearch and get first three items with best score
        movies=es.search(
            index='western',
            body={"query": {
                    "multi_match": {
                        "fields":  [ "title", "plot" ],
                        "query": query,
                        "fuzziness": "AUTO"
                    }
                },
                "highlight": {
                    "fields": {
                        "title": {"number_of_fragments": 0},
                        "plot": {"number_of_fragments": 0}
                    }
                }
            },
            size=3
        )

        return render_template("home.html", western=movies)

if __name__ == "__main__":
    app.run()
    # Clear movie index from ElasticSearch
    es.indices.delete(index='western', ignore=[400, 404])
