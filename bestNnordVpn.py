import json
import requests

try:
    response = requests.get("https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations")
    response.raise_for_status()
    data=response.json()
    print(data[0]['hostname'])
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

