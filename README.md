# Closest Restaurant Flask API
## Requirements
- System: [Docker and Docker Compose](https://docs.docker.com/compose/install/)
- Places API: [Google Cloud Console Setup](https://developers.google.com/maps/documentation/places/web-service/cloud-setup)
## Usage
Follow these steps in the root directory of
your local repository:
- Rename the ```.env.template``` file to ```.env```.
- Set the environment variable [GOOGLE_API_KEY](https://developers.google.com/maps/documentation/places/web-service/get-api-key) in ```.env``` file.
- Run the following command:
    ```
    docker-compose up
    ```
- Replacing the query parameters with your choices, send a GET HTTP request to the following URL:
    ```
    http://localhost:5000/?city=<city_name>&lat=<latitude>&long=<longitude>
    ```
## API Documentation UIs
[OpenAPI](https://www.openapis.org/about) specification is available in [Swagger](http://localhost:5000/docs) and [Redoc](http://localhost:5000/redoc).
