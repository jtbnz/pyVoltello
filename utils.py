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
    ##request_data = dump.dump(response.request)
    ##print(request_data.decode('utf-8')) 
        
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.json()['Message']}")
        return None         