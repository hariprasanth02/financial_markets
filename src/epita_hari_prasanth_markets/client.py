
import requests

from epita_hari_prasanth_markets.config import config


BASE_URL = "https://finnhub.io/api/v1"


def fetch_live_data() -> dict:

    # Validate API key
    config.validate()

    # API endpoint
    url = f"{BASE_URL}/quote"

    # Authentication header
    headers = {
        "X-Finnhub-Token": config.api_key
    }

    # Query parameters
    params = {
        "symbol": "NVDA"
    }

    # Send GET request
    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    # Raise error for unsuccessful HTTP response
    response.raise_for_status()

    # Convert JSON response into Python dictionary
    data = response.json()

    # Return formatted market information
    return {
        "status": "LIVE_SUCCESS",
        "symbol": "NVDA",
        "company": "NVIDIA",
        "current_price": data.get("c"),
        "change": data.get("d"),
        "change_percent": data.get("dp"),
        "high": data.get("h"),
        "low": data.get("l"),
        "open": data.get("o"),
        "previous_close": data.get("pc"),
        "timestamp": data.get("t")
    }
