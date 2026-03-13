import time
import requests


def fetch_btc_price(retries: int = 3, delay: int = 5) -> float:
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    last_error = None

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            price = data["bitcoin"]["usd"]

            return float(price)

        except requests.RequestException as e:
            last_error = e

            if attempt < retries:
                print(f"API request failed on attempt {attempt}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"API request failed after {retries} attempts.")
                raise last_error