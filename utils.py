import requests
from secrets import API_TOKEN, CUSTOMER_ID, UTILITY_ID

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID

base_url = "https://acapi.vecddevau1.village.energy/xv1"
service_points_endpoint = "/get/customer/energy/electricity/servicepoints/"
securityContext = "Voltello/CUSTOMERS/Individual/"


headers = {
    "apiKey": API_TOKEN,
    "Accept": "*/*",
    "Content-Type": "application/json"
}

def get_service_points_list(customer_id):
    url = f"{base_url}{service_points_endpoint}{securityContext}{customer_id}"
    params = {
        "customerId": customer_id,
        "utilityIdentifier": UTILITY_ID
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None

def get_service_points_detail(servicepointID):
    url = f"{base_url}{service_points_endpoint}{servicepointID}/usage/{securityContext}{CUSTOMER_ID}"
    print(url)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None

def get_live_data(servicepointID):
    url = f"{base_url}{service_points_endpoint}{servicepointID}/usage/{securityContext}{CUSTOMER_ID}"
    print(url)
    params = {
        "action": "getPowerForServicePoint",
        "returnFormat": "VE"
    }
    response = requests.get(url, headers=headers, params=params)
        
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None
    
def get_service_points_der(servicepointID):

    url = f"{base_url}{service_points_endpoint}{servicepointID}/der/{securityContext}{customer_id}/"
    print (url)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None    

def get_service_points_usage(servicepointID, from_date, to_date, returnAllTelemetry, returnData):

    url = f"{base_url}{service_points_endpoint}{servicepointID}/usage/{securityContext}{customer_id}/"
    params = {
        "fromDate": from_date,
        "toDate": to_date,
        "returnAllTelemetry": returnAllTelemetry,
        "returnData": returnData
    }
    
    response = requests.get(url, headers=headers, params=params)
        
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None
    
            