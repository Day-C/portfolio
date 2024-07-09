#!/usr/bin/python3
"""flask app."""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/", strict_slaches=False)
def index():
    """Home"""

    return render_template("index.html")
