#!/usr/bin/env python3
"""contains flask app"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def json_payload():
    """
    returns a json payload
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
