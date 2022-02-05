# Everactive API Client Sample - Python 3.9

A sample client using Python `requests` and `requests_oauthlib` to retrieve a list of steam traps.

## Configuration
To use this sample you must have a `client_credentials` grant_type `client_id` and `client_secret` provided by Everactive. These must be assigned to environment variables `EVERACTIVE_CLIENT_ID` and `EVERACTIVE_CLIENT_SECRET`, respectively. The environment variable `EVERACTIVE_API_URL` must be set to the Everactive API base url. The environment variable `EVERACTIVE_AUTH_URL` must be set to the Everactive token url.  Lastly, the environment variable `EVERACTIVE_AUDIENCE` must be set to the Everactive Oauth2 audience.

## Running the application
To install the dependencies run
```cmd
pip install -r requirements.txt
```

To execute the Steamtrap example
```cmd
EVERACTIVE_AUTH_URL="https://auth.insights.everactive.com/oauth/token" \
    EVERACTIVE_API_URL="https://api.data.everactive.com/v2020-07" \
    EVERACTIVE_CLIENT_ID="YOUR CLIENT ID" \
    EVERACTIVE_CLIENT_SECRET="YOUR CLIENT SECRET" \
    EVERACTIVE_AUDIENCE="https://everactive/audience"
    python api_service.py
```

## Running with Docker

In case you don't want to use a local Python environment, a Dockerfile is included that runs the application inside a container.

To Build:

```cmd
docker build -t python_api/test .
```

To Run:

```cmd
docker run \
-it \
--rm \
--env EVERACTIVE_AUTH_URL="https://auth.insights.everactive.com/oauth/token" \
--env EVERACTIVE_API_URL="https://api.data.everactive.com/v2020-07" \
--env EVERACTIVE_CLIENT_ID="YOUR CLIENT ID" \
--env EVERACTIVE_CLIENT_SECRET="YOUR CLIENT SECRET" \
--env EVERACTIVE_AUDIENCE="https://everactive/audience" \
python_api/test
```
