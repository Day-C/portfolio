#!/usr/bin/python3
"""flask app."""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    """Home"""

    return render_template("search_drug.html")

if __name__ == "__main__":
    app.run(debug=True)
