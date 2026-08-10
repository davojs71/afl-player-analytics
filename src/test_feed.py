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

    text = response.text

    search_terms = [
        "playerStats",
        "player_stats",
        "statistics",
        "matchStats",
        "stats",
        "CD_C",
        "8123"
    ]

    for term in search_terms:
        print(f"\n--- Searching for: {term} ---")
        position = text.find(term)

        if position >= 0:
            print("FOUND at position:", position)
            print(text[max(0, position - 500):position + 1500])
        else:
            print("Not found")


if __name__ == "__main__":
    main()
