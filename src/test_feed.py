import requests


def fetch(url):
    headers = {
        "User-Agent": "Davo-AFL-Stats/1.0 (personal research project)"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    print("\n========================================")
    print(url)
    print("========================================")
    print("Status:", response.status_code)
    print(response.text[:30000])


def main():

    base = "https://www.footyinfo.com/assets/"

    files = [
        "stats-DwgRxqhL.js",
        "stats-table-ChJkV7O8.js",
        "stats-verification-service-rbM6ULUE.js",
        "stats-Dts8JUIc.js",
    ]

    for filename in files:
        fetch(base + filename)


if __name__ == "__main__":
    main()
