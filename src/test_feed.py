import requests


def main():
    url = "https://api.afl.com.au/statspro"

    headers = {
        "User-Agent": "Davo-AFL-Stats/1.0 (personal research project)",
        "Accept": "application/json"
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
