""" Blueprint for workflow endpoint """

import requests
from flask import Blueprint, jsonify
from src.conf import GITHUB_REPOSITORY, GITHUB_WORKFLOW_ID, GITHUB_TOKEN

workflow_bp = Blueprint("workflow", __name__)


@workflow_bp.route("/workflow", methods=["POST"])
def workflow() -> jsonify:
    """
    Trigger GitHub workflow
    :return: Workflow trigger status
    """
    if not GITHUB_TOKEN:
        return jsonify({"error": "GitHub token is not set"}), 500
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/actions/workflows/{GITHUB_WORKFLOW_ID}/dispatches"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = {
        "ref": "main",
        "inputs": {
            "greeting": "Good morning",
            "from-flask": "true",
            "environment": "Test",
        },
    }
    response = requests.post(url, headers=headers, json=data, timeout=10)
    if response.status_code == 204:
        return jsonify({"message": "Workflow triggered successfully"}), 200
    return (
        jsonify({"error": "Failed to trigger workflow", "details": response.json()}),
        response.status_code,
    )
