import requests


def main():
    url = "https://www.afl.com.au/matches/8123"

    headers = {
        "User-Agent": "Davo-AFL-Stats/1.0 (personal research project)"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    print("Status:", response.status_code)
    print(response.text[:5000])


if __name__ == "__main__":
    main()
