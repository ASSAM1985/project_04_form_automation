import requests
import time

url = "https://books.toscrape.com/"

print("Website Monitor Started...")

old_status = None

while True:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            new_status = "ONLINE"
        else:
            new_status = "OFFLINE"

        if old_status is None:
            print("Current Status:", new_status)

        elif new_status != old_status:
            print("Status Changed!")
            print("New Status:", new_status)

        old_status = new_status

    except Exception as e:
        print("Error:", e)

    time.sleep(10)