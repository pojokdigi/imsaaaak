import requests

url = "https://equran.id/api/v2/imsakiyah/provinsi"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Do something with the response data
else:
    print("Failed to get data from the API.")
