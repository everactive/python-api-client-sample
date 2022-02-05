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
            EVERACTIVE_AUTH_URL
            EVERACTIVE_API_URL
            EVERACTIVE_CLIENT_ID
            EVERACTIVE_CLIENT_SECRET
            EVERACTIVE_AUDIENCE
        """
        self._auth_url = os.environ.get("EVERACTIVE_AUTH_URL")
        self._base_url = os.environ.get("EVERACTIVE_API_URL")
        self._client_id = os.environ.get("EVERACTIVE_CLIENT_ID")
        self._client_secret = os.environ.get("EVERACTIVE_CLIENT_SECRET")
        self._audience = os.environ.get("EVERACTIVE_AUDIENCE")
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
        print(f"Authenticating to Everactive API ({self._auth_url})")
        self._session.fetch_token(
            token_url=self._auth_url,
            client_id=self._client_id,
            client_secret=self._client_secret,
            audience=self._audience,
            include_client_id=True,
        )

    def get_steam_traps(self):
        url = self._base_url + "steamtraps"
        print(f"Fetching steam traps from {url}")

        response = self._session.request("GET", url)
        result = response.json()

        print(f"PaginationInfo: {result['paginationInfo']}")

        return result["data"]


if __name__ == "__main__":
    api = ApiService()
    traps = api.get_steam_traps()
    print(f"Returned {len(traps)} steam traps (first page only).")
