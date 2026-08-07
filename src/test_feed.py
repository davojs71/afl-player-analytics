response = requests.get(
    url,
    params=params,
    headers={
        "User-Agent": "Davo-AFL-Stats/1.0 (personal research project)"
    },
    timeout=30
)

def main():
    url = "https://api.squiggle.com.au/"

    params = {
        "q": "games",
        "year": 2026
    }

    response = requests.get(url, params=params)

    print("Status:", response.status_code)
    print(response.text[:1000])


if __name__ == "__main__":
    main()
