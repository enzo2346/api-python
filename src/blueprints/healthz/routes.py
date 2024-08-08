""" Blueprint for health check endpoint """

from flask import Blueprint

healthz_bp = Blueprint("healthz", __name__)


@healthz_bp.route("/healthz", methods=["GET"])
def hello_world() -> str:
    """
    Health check endpoint
    :return: Hello, world!
    """
    return "Hello, world!"
