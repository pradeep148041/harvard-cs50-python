import sys
import requests  # Don't forget to import the 'requests' module

# Check if the correct number of command-line arguments is provided
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a valid number")
        sys.exit(1)
else:
    print("Missing or incorrect command-line argument")
    sys.exit(1)

try:
    # Fix the URL by removing the extra comma at the end
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r.raise_for_status()  # Check for request errors

    response = r.json()

    # Use the 'value' obtained from the command line in the calculation
    bitcoin_rate = response['bpi']['USD']['rate_float']
    total_amount = bitcoin_rate * value

    print(f"${total_amount:,.4f}")
except requests.RequestException as e:
    print(f"RequestException: {e}")
    sys.exit(1)
except KeyError:
    print("Error in parsing API response")
    sys.exit(1)
except ValueError:
    print("Error in converting API response to JSON")
    sys.exit(1)
