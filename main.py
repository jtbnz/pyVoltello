import requests
import json
from requests_toolbelt.utils import dump
from secrets import API_TOKEN, CUSTOMER_ID, UTILITY_ID

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID
securityContext = "Voltello/CUSTOMERS/Individual/"

#base_url = "https://cddevapi.village.energy/xv1"
base_url = "https://acapi.vecddevau1.village.energy/xv1"

service_points_endpoint = "/get/customer/energy/electricity/servicepoints/"
headers = {
    "apiKey": API_TOKEN,
    "Accept": "*/*",
    "Content-Type": "application/json"
}

#  get service points list
def get_service_points_list(customer_id):
    # Endpoint 
    url = f"{base_url}{service_points_endpoint}{securityContext}{customer_id}"
    params = {
        "customerId": customer_id,
       # "utilityIdentifier": utility_id
    }
    response = requests.get(url, headers=headers, params=params)
    
    print (url)
    #data = dump.dump_all(response)
    #print(data.decode('utf-8'))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None

#  get usage
def get_service_points_usage(servicepointID, from_date, to_date, returnAllTelemetry, returnData):
    # /get/energy/electricity/servicepoints/{servicePointId}/usage/{securityContext}
    url = f"{base_url}/get/energy/electricity/servicepoints/{servicepointID}/usage/{securityContext}{customer_id}/"
    params = {
        "fromDate": from_date,
        "toDate": to_date,
        "returnAllTelemetry": returnAllTelemetry,
        "returnData": returnData
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    data = dump.dump_all(response)
    print(data.decode('utf-8'))
        
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None
    
# Get the service points list
service_points_list = get_service_points_list(CUSTOMER_ID)
print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------    Service Points List   -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")
print ("")
print(json.dumps(service_points_list, indent=4))
print ("")


# Extract servicePointID correctly
print ("-------------------------------------------------------------------------------------------------")
print ("------------------------------       Service Usage      -----------------------------------------")
print ("-------------------------------------------------------------------------------------------------")

servicePointID = service_points_list['data']['servicePoints'][0]['servicePointId']
print ("")
print(" servicePointID: ", servicePointID)
print ("")

# Get Usage
from_date = "2024-11-10"
to_date = "2024-11-11"
returnAllTelemetry = "false"
returnData = "dailyTotal" # aligned5MinRead, aligned15MinRead, aligned30MinRead, alignedHourlyRead, dailyTotal
usage_list = get_service_points_usage(servicePointID, from_date, to_date, returnAllTelemetry, returnData)




