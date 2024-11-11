import requests
from requests_toolbelt.utils import dump
from secrets import API_TOKEN, CUSTOMER_ID, UTILITY_ID

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID

# Base URL for the API
#base_url = "https://cddevapi.village.energy/xv1"
base_url = "https://acapi.vecddevau1.village.energy/xv1"

# Endpoint for getting service points list
service_points_endpoint = "/get/customer/energy/electricity/servicepoints/Voltello/CUSTOMERS/Individual/"

# Headers for the request
headers = {
    "apiKey": API_TOKEN,
    "Accept": "*/*",
    "Content-Type": "application/json"
}

# Function to get service points list
def get_service_points_list(customer_id):
    url = f"{base_url}{service_points_endpoint}{customer_id}"
    params = {
        "customerId": customer_id,
       # "utilityIdentifier": utility_id
    }
    response = requests.get(url, headers=headers, params=params)
    
    data = dump.dump_all(response)
    print(data.decode('utf-8'))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['message']}")

        
        return None

# Get the service points list
service_points_list = get_service_points_list(CUSTOMER_ID)
print(service_points_list)


