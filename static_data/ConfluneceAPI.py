import requests
import json

if __name__ == '__main__':
    url = "http://{baseurl}/confluence/rest/api/accessmode"

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))