import requests
import sys

def main():
    if len(sys.argv) == 2:

        try:
            amount = float(sys.argv[1])
            print(convert(amount))
        except ValueError:
            sys.exit("Command-line argument is not a number")

    else:
        sys.exit("Missing command-line argument")


def convert(n):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        sum = price * n
        return f"${sum:,.4f}"
    except requests.RequestException:
        pass


main()