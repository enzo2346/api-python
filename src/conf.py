""" Configuration file for the Flask app """

import os

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", "5000")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

GITHUB_REPOSITORY = "enzo2346/simple-flask-app"
GITHUB_WORKFLOW_ID = "greeting.yml"
