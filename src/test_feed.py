import requests


def main():
    url = "https://www.footyinfo.com/assets/stats-Dts8JUIc.js"

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

    searches = [
        "createServerFn",
        "handler",
        "game",
        "match",
        "player",
        "stats",
        "gameLog",
        "gameLogs",
        "statistics",
        "playerStats",
        "matchStats",
    ]

    for term in searches:
        print("\n--- Searching for:", term, "---")

        position = text.lower().find(term.lower())

        if position == -1:
            print("Not found")
        else:
            print("FOUND at position:", position)
            start = max(0, position - 500)
            end = min(len(text), position + 1500)
            print(text[start:end])


if __name__ == "__main__":
    main()
