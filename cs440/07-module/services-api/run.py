from flask import Flask
from flask_restx import Api
from app.endpoints import ns as service_namespace

app = Flask(__name__)
api = Api(
    app,
    title="Service Endpoints API",
    version="1.0",
    description="Manage and test internal/external service endpoints",
    doc="/docs"
)

api.add_namespace(service_namespace, path="/services")

if __name__ == "__main__":
    app.run(debug=True)
