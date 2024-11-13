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
    
    #print (url)
    #data = dump.dump_all(response)
    #print(data.decode('utf-8'))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None


def get_service_points_detail(servicepointID):
    # Endpoint 
    url = f"{base_url}{service_points_endpoint}/{servicePointID}/{securityContext}"
   
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None


#  get usage
def get_service_points_usage(servicepointID, from_date, to_date, returnAllTelemetry, returnData):

    url = f"{base_url}/get/customer/energy/electricity/servicepoints/{servicepointID}/usage/{securityContext}{customer_id}/"
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
    
# Get the service points list

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
print ("------------------------------     Service Usage Today  -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
from_date = datetime.today().strftime('%Y-%m-%d')
to_date = datetime.today().strftime('%Y-%m-%d')
returnAllTelemetry = "true"
returnData = "dailyTotal" # aligned5MinRead, aligned15MinRead, aligned30MinRead, alignedHourlyRead, dailyTotal
usage_list = get_service_points_usage(servicePointID, from_date, to_date, returnAllTelemetry, returnData)
print(json.dumps(usage_list, indent=4))


print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------     Service Usage Now    -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
from_date = datetime.today().strftime('%Y-%m-%d')
to_date = datetime.today().strftime('%Y-%m-%d')
returnAllTelemetry = "true"
returnData = "aligned5MinRead" # aligned5MinRead, aligned15MinRead, aligned30MinRead, alignedHourlyRead, dailyTotal
usage_list = get_service_points_usage(servicePointID, from_date, to_date, returnAllTelemetry, returnData)
print(json.dumps(usage_list, indent=4))





