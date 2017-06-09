import pandas as pd
import numpy as np
import sklearn
from imdb import IMDb
from flask import Flask, render_template, request
# from elasticsearch import ElasticSearch

app = Flask(__name__)

# Get movie dataframe
df = pd.read_csv('western.csv', sep=';')

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        movies = {}
        for i in range(len(df)):
            movies[df["title"][i]] = df["plot"][i]

        return render_template("movie.html", d = movies)

if __name__ == "__main__":
    app.run()
