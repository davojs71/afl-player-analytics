import requests

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
