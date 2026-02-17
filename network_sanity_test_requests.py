import requests
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv(dotenv_path="api_keys/protection.env")
PROXY_USERNAME = os.getenv("PROXY_USERNAME", "")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD", "")
PROXY_HOST_PORT = "127.0.0.1:9000"

# Encode credentials safely
encoded_user = urllib.parse.quote(PROXY_USERNAME)
encoded_pass = urllib.parse.quote(PROXY_PASSWORD)

proxy_url = f"http://{encoded_user}:{encoded_pass}@{PROXY_HOST_PORT}"

proxies = {
    "http": proxy_url,
    "https": proxy_url,
}


def test_proxy():
    print("Testing proxy...")
    try:
        # https://jsonplaceholder.typicode.com/users
        # https://catfact.ninja/fact
        # https://dog.ceo/api/breeds/image/random
        # https://api.ipify.org?format=json
        response = requests.get("https://catfact.ninja/fact", proxies=proxies, timeout=10)
        response.raise_for_status()
        fun_fact = response.json().get("fact")
        print(f"Proxy is working. Your cat fact is : {fun_fact}")
        return True
    except requests.exceptions.ProxyError as e:
        print("Proxy error:", e)
    except requests.exceptions.ConnectTimeout:
        print("Proxy timed out.")
    except Exception as e:
        print("Other error:", e)
    return False

if __name__ == '__main__':
    test_proxy()