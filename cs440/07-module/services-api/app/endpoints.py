from flask import request
from flask_restx import Namespace, Resource, fields
import json
import os
import requests

ns = Namespace("services", description="Service endpoint configuration")
CONFIG_FILE = "services.json"

# Preloaded sample data
def load_services():
    if not os.path.exists(CONFIG_FILE):
        sample = {
            "auth_service": {
                "url": "https://example.com/auth",
                "health_check": "/ping",
                "env": "production"
            },
            "user_service": {
                "url": "https://example.com/users",
                "health_check": "/status",
                "env": "staging"
            }
        }
        save_services(sample)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_services(services):
    with open(CONFIG_FILE, "w") as f:
        json.dump(services, f, indent=2)

service_model = ns.model("Service", {
    "name": fields.String(required=True),
    "url": fields.String(required=True),
    "health_check": fields.String(required=True),
    "env": fields.String(required=True, enum=["dev", "staging", "production"])
})

@ns.route("/")
class ServiceList(Resource):
    def get(self):
        """List all services grouped by environment"""
        services = load_services()
        grouped = {"dev": {}, "staging": {}, "production": {}}
        for name, svc in services.items():
            grouped[svc["env"]][name] = svc
        return grouped

    @ns.expect(service_model)
    def post(self):
        """Add a new service"""
        data = request.json
        services = load_services()
        services[data["name"]] = {
            "url": data["url"],
            "health_check": data["health_check"],
            "env": data["env"]
        }
        save_services(services)
        return {"message": "Service added"}, 201

@ns.route("/<string:name>")
@ns.param("name", "Service name")
class Service(Resource):
    def get(self, name):
        """Get service details"""
        services = load_services()
        if name in services:
            return services[name]
        ns.abort(404, "Service not found")

    @ns.expect(service_model)
    def put(self, name):
        """Update service info"""
        services = load_services()
        if name not in services:
            ns.abort(404, "Service not found")
        data = request.json
        services[name] = {
            "url": data["url"],
            "health_check": data["health_check"],
            "env": data["env"]
        }
        save_services(services)
        return {"message": "Service updated"}

    def delete(self, name):
        """Remove a service"""
        services = load_services()
        if name in services:
            del services[name]
            save_services(services)
            return {"message": "Service deleted"}
        ns.abort(404, "Service not found")

@ns.route("/<string:name>/check")
@ns.param("name", "Service name")
class ServiceHealth(Resource):
    def get(self, name):
        """Check health of a service"""
        services = load_services()
        if name not in services:
            ns.abort(404, "Service not found")
        svc = services[name]
        try:
            response = requests.get(svc["url"] + svc["health_check"], timeout=2)
            return {
                "status": response.status_code,
                "response": response.text
            }
        except Exception as e:
            return {
                "status": "unreachable",
                "error": str(e)
            }
