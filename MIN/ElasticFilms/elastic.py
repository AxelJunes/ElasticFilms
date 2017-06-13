import pandas as pd
import numpy as np
import sklearn
import requests
import json
from imdb import IMDb
from flask import Flask, render_template, request
from elasticsearch import ElasticSearch

app = Flask(__name__)

# Get movie dataframe
df = pd.read_csv('western.csv', sep=';')

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        res = requests.get('http://localhost:9200')
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        r = requests.get('http://localhost:9200')
        i = 1
        while r.status_code == 200:
            r = requests.get('https://api.themoviedb.org/3/movie/550?api_key=f93291a0157ffd416fde2b0ba87d6a4c'+ str(i))
            es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
            i=i+1
        http://www.omdbapi.com/?apikey=[yourkey]&
        return render_template("home.html")
    else:
        movies = {}
        for i in range(len(df)):
            movies[df["title"][i]] = df["plot"][i]

        return render_template("movie.html", d = movies)

if __name__ == "__main__":
    app.run()
