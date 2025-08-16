import requests
import json
import sys
if len(sys.argv) != 2:
    sys.exit(1)
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=d4a923918bdfad7df4ae69c13f9dcfbd59c21da1ddb1ae4c6bb3c6cf26bc7da4" )
    amount = response.json()
    total = float(amount["data"]["priceUsd"])*float(sys.argv[1])
    print(f"${total:,.4f}")

except (requests.RequestException,ValueError):
    print("Command-line argument is not a number")
    sys.exit(1)
