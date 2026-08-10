import requests


def main():
    url = "https://api.squiggle.com.au/"

    params = {
        "q": "games",
        "year": 2026
    }

    headers = {
        "User-Agent": "Davo-AFL-Stats/1.0 (personal research project)"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    print("Status:", response.status_code)
    print(response.text[:2000])


if __name__ == "__main__":
    main()
