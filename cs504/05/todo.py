import os
from flask import Flask, jsonify, request

def create_app():
    """Create and configure the Flask app with multiple routes."""
    app = Flask(__name__)

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)