import requests
import json
from requests_toolbelt.utils import dump
from secrets import API_TOKEN, CUSTOMER_ID, UTILITY_ID
from datetime import datetime

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID

securityContext = "Voltello/CUSTOMERS/Individual/"
base_url = "https://acapi.vecddevau1.village.energy/xv1"
service_points_endpoint = "/get/customer/energy/electricity/servicepoints/"

headers = {
    "apiKey": API_TOKEN,
    "Accept": "*/*",
    "Content-Type": "application/json"
}

def get_service_points_list(customer_id):
    # Endpoint 
    url = f"{base_url}{service_points_endpoint}{securityContext}{customer_id}"
    params = {
        "customerId": customer_id
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None

def get_service_points_detail(servicepointID):
    # Endpoint 
    url = f"{base_url}{service_points_endpoint}{servicePointID}/{securityContext}{customer_id}"
    print (url)
    response = requests.get(url, headers=headers)
    
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
    
def get_live_data(servicepointID):
    #apiPath="/get/customer/energy/electricity/servicepoints/${servicePointId}/usage/${customerSecurityContext}?action=getPowerForServicePoint&returnFormat=VE"
    url = f"{base_url}{service_points_endpoint}{servicepointID}/usage/{securityContext}{customer_id}"
    print (url)
    params = {
        "action": "getPowerForServicePoint",
        "returnFormat": "VE"
    }
    

    response = requests.get(url, headers=headers, params=params)
    request_data = dump.dump(response.request)
    print(request_data.decode('utf-8')) 
        
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None         
    

print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------    Service Points List   -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
service_points_list = get_service_points_list(CUSTOMER_ID)
print(json.dumps(service_points_list, indent=4))
servicePointID = service_points_list['data']['servicePoints'][0]['servicePointId']

print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------    Service Points Detail -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
service_points_list = get_service_points_detail(servicePointID)
print(json.dumps(service_points_list, indent=4))

print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------    Service Points DER -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
service_points_der = get_service_points_der(servicePointID)
print(json.dumps(service_points_list, indent=4))

print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------     Service Usage Today  -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
from_date = datetime.today().strftime('%Y-%m-%d')
to_date = datetime.today().strftime('%Y-%m-%d')
returnAllTelemetry = "true"
returnData = "dailyTotal" # alignedminRead, aligned15minRead, aligned30minRead, alignedHourlyRead, dailyTotal
usage_list = get_service_points_usage(servicePointID, from_date, to_date, returnAllTelemetry, returnData)
print(json.dumps(usage_list, indent=4))


print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------     Service Usage 5Min    -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
from_date = datetime.today().strftime('%Y-%m-%d')
to_date = datetime.today().strftime('%Y-%m-%d')
returnAllTelemetry = "true"
returnData = "aligned5minRead" 
usage_list = get_service_points_usage(servicePointID, from_date, to_date, returnAllTelemetry, returnData)
print(json.dumps(usage_list, indent=4))

print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------     Service Usage 15Min    -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
from_date = datetime.today().strftime('%Y-%m-%d')
to_date = datetime.today().strftime('%Y-%m-%d')
returnAllTelemetry = "true"
returnData = "aligned15minRead"
usage_list = get_service_points_usage(servicePointID, from_date, to_date, returnAllTelemetry, returnData)
print(json.dumps(usage_list, indent=4))

print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------          Live Data       -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
live_data = get_live_data(servicePointID)
print(json.dumps(live_data, indent=4))

