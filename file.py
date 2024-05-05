import requests
import json

def get_inventory_details(api_token):
    # Replace these URLs with your FortiManager API endpoints
    base_url = "https://your_fortimanager_ip/api/v2/cmdb/"
    inventory_url = base_url + "system/global/inventory"
    
    # Set up request headers with API token
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    try:
        # Send GET request to retrieve inventory details
        response = requests.get(inventory_url, headers=headers, verify=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes

        # Parse JSON response
        inventory_data = response.json()

        # Print inventory details
        print("Inventory Details:")
        for item in inventory_data.get("results", []):
            print(f"Name: {item.get('name')}")
            print(f"Serial Number: {item.get('serial_number')}")
            print(f"Model: {item.get('model')}")
            print(f"Firmware Version: {item.get('firmware_version')}")
            print("-----------------------------------------")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace "YOUR_API_TOKEN" with your actual API token
    api_token = "YOUR_API_TOKEN"
    get_inventory_details(api_token)
