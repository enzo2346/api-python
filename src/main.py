
from flask import Flask, render_template, jsonify
from flasgger import Swagger
from src.conf import HOST, PORT
from .blueprints.home.routes import home_bp
from .blueprints.healthz.routes import healthz_bp
from .blueprints.workflow.routes import workflow_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(healthz_bp)
app.register_blueprint(workflow_bp)

swagger = Swagger(app, template_file='swagger.yaml')

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)