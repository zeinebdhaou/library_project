import os
import connexion
from flask import send_from_directory, jsonify
from swagger_server import encoder

def main():
    # Create the Connexion application
    app = connexion.App(__name__, specification_dir='./swagger/')

    # Set the JSON encoder
    app.app.json_encoder = encoder.JSONEncoder

    # Add the API defined by the Swagger specification
    app.add_api('swagger.yaml', arguments={'title': 'Library API Spec'}, pythonic_params=True)

    # Serve the HTML file (ensure the static folder contains your index.html)
    @app.route('/')
    def serve_index():
        return send_from_directory('static', 'index.html')

    # Run the application
    app.run(port=8080)  # Removed debug=True as it's not supported in uvicorn

if __name__ == '__main__':
    main()
