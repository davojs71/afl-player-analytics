import os
import requests
from datetime import datetime


def main():

    url = os.environ["GOOGLE_SCRIPT_URL"]

    payload = {
        "season": "2026",
        "player": "SYSTEM TEST",
        "test": "Connection successful",
        "time": str(datetime.now())
    }

    response = requests.post(
        url,
        json=payload
    )

    print(response.text)


if __name__ == "__main__":
    main()
