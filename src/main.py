import requests
from flask import Flask, render_template, jsonify
from src.conf import HOST, PORT, GITHUB_TOKEN, GITHUB_REPOSITORY, GITHUB_WORKFLOW_ID
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/home")
def home():
    return render_template("index.html", title="Home")

@app.route("/workflow")
def workflow():
    if not GITHUB_TOKEN:
        return jsonify({"error": "GitHub token is not set"}), 500
    url = f'https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/workflows/{GITHUB_WORKFLOW_ID}/dispatches'
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    data = {
        'ref': 'main',
        'inputs': {
            'logLevel':'info',
            'tags':'true',
            'environment':'Test'
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 204:
        return jsonify({"message": "Workflow triggered successfully"}), 200
    else:
        return jsonify({"error": "Failed to trigger workflow", "details": response.json()}), response.status_code


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)