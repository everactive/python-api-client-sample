from oauthlib.oauth2 import BackendApplicationClient
import os
from requests.adapters import HTTPAdapter
from requests_oauthlib import OAuth2Session
from urllib.parse import urljoin


class ApiService:
    def __init__(
        self,
    ):
        """Create a new connection to Everactive API.

        Arguments: None

        Reads Environment variables:
            EVERACTIVE_API_URL
            EVERACTIVE_CLIENT_ID
            EVERACTIVE_CLIENT_SECRET
        """
        self._base_url = os.environ.get("EVERACTIVE_API_URL")
        self._client_id = os.environ.get("EVERACTIVE_CLIENT_ID")
        self._client_secret = os.environ.get("EVERACTIVE_CLIENT_SECRET")
        self._session = None

        if not self._base_url or not self._client_id or not self._client_secret:
            raise EnvironmentError(
                "EVERACTIVE_API_URL, EVERACTIVE_CLIENT_ID and EVERACTIVE_CLIENT_SECRET environment variables must be defined"
            )

        if self._base_url and not self._base_url.endswith("/"):
            self._base_url += "/"

        adapter = HTTPAdapter(max_retries=3)
        client = BackendApplicationClient(client_id=self._client_id)
        self._session = OAuth2Session(client=client)
        self._session.mount(self._base_url, adapter)
        self._authenticate()

    def __del__(self):
        """Close session when object is deleted."""
        if self._session:
            self._session.close()

    def _authenticate(self):
        token_url = urljoin(self._base_url, "auth/token")
        print(f"Authenticating to Everactive API ({token_url})")
        self._session.fetch_token(
            token_url=token_url,
            client_id=self._client_id,
            client_secret=self._client_secret,
            include_client_id=True,
        )

    def get_sensors(self):
        url = self._base_url + "ds/v1/eversensors"
        print(f"Fetching eversensors from {url}")
        response = self._session.request("GET", url)
        result = response.json()
        print(f"PaginationInfo: {result['paginationInfo']}")
        return result["data"]


if __name__ == "__main__":
    api = ApiService()
    sensors = api.get_sensors()
    print(f"Returned {len(sensors)} eversensors (first page only).")
    print(sensors)
