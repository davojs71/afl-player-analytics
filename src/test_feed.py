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
    print(response.text[:30000])


if __name__ == "__main__":
    main()
