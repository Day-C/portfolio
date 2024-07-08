#!/usr/bin/python3
"""Flask app."""
from flask import Flask, render_template
import requests


app = Flask(__name__)

def get_names():
    """get drug names"""

    url = "https://api.fda.gov/drug/label.json?limit=1000"

    names = []
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        for item in response["results"]:
            name = item["openfda"].get("brand_name")
            if name != None:
                names.append(name[0])
        print("done!")
        return names

@app.route('/', strict_slashes=False)
def home():
    #Home page.

    names = get_names()
    return render_template("index.html", drugs=names)


if __name__ == "__main__":
    app.run(debug=True)
