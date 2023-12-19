import requests
import sys


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    num_btc = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    data = response.json()
    btc_price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit()

cost = num_btc * btc_price
print(f"${cost:,.4f}")
