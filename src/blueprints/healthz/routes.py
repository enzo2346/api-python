from flask import Blueprint

healthz_bp = Blueprint('healthz', __name__)

@healthz_bp.route("/healthz", methods=['GET'])
def hello_world():
    return "Hello, world!"