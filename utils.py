import requests
from config import API_TOKEN, CUSTOMER_ID, UTILITY_ID

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
    response = requests.get(url, headers=headers)                                                                          
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None

def get_live_data(servicepointID):

    url = f"{base_url}{service_points_endpoint}{servicepointID}/usage/realtime/{securityContext}{CUSTOMER_ID}"
    response = requests.get(url, headers=headers)
    
        
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None
    
def get_service_points_der(servicepointID):

    url = f"{base_url}{service_points_endpoint}{servicepointID}/der/{securityContext}{customer_id}/"
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
    
def get_displayed_data(live_data):
    displayed_data = {}
    flow_data = live_data['data']['flowData']
    is_displayed = flow_data['isDisplayed']
    power_data = flow_data['power']

    if is_displayed['grid']:
        displayed_data['grid'] = power_data['grid']['power']
    if is_displayed['solar']:
        displayed_data['solar'] = {
            'power': power_data['solar']['power'],
            'name': power_data['solar']['endPoints'][0]['nickName']
        }
    if is_displayed['battery']:
        displayed_data['battery'] = {
            'power': power_data['battery']['power'],
            'stateOfCharge': power_data['battery']['endPoints'][0]['stateOfCharge']
        }
    if is_displayed['home']:
        displayed_data['home'] = power_data['home']['power']
    if is_displayed['ev']:
        displayed_data['ev'] = power_data['ev']['power']

    return displayed_data        