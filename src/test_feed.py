import requests


def main():
    urls = [
        "https://aflapi.afl.com.au/afl/v2/matches/8123",
        "https://aflapi.afl.com.au/afl/v2/matches/8123/players",
        "https://aflapi.afl.com.au/afl/v2/matches/8123/player-stats",
        "https://aflapi.afl.com.au/afl/v2/matches/8123/statistics",
        "https://aflapi.afl.com.au/afl/v2/matches/8123/teams",
    ]

    headers = {
        "User-Agent": "Davo-AFL-Stats/1.0 (personal research project)",
        "Accept": "application/json"
    }

    for url in urls:
        print("\n================================")
        print(url)
        print("================================")

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=30
            )

            print("Status:", response.status_code)
            print(response.text[:2000])

        except Exception as e:
            print("ERROR:", e)


if __name__ == "__main__":
    main()
