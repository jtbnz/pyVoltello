import requests
from secrets import API_TOKEN

# Define the base URL and endpoints
base_url = "https://cddevapi.village.energy/xv1"
service_points_endpoint = "/get/energy/electricity/servicepoints/{securityContext}"
service_point_usage_endpoint = "/get/energy/electricity/servicepoints/{servicePointId}/usage/{securityContext}"

# Define the headers
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}

# Function to get service points
def get_service_points(security_context):
    url = base_url + service_points_endpoint.format(securityContext=security_context)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["servicePoints"]
    else:
        print(f"Error: {response.json()['message']}")
        return None

# Function to get service point usage
def get_service_point_usage(service_point_id, security_context, from_date, to_date):
    url = base_url + service_point_usage_endpoint.format(servicePointId=service_point_id, securityContext=security_context)
    params = {
        "fromDate": from_date,
        "toDate": to_date,
        "returnAllTelemetry": False,
        "returnData": "alignedHourlyRead"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Error: {response.json()['message']}")
        return None


security_context = "VE/TELEMETRY/abc/xyz"
print(security_context)
service_points = get_service_points(security_context)
if service_points:
    service_point_id = service_points["servicePointId"]
    usage_data = get_service_point_usage(service_point_id, security_context, "2023-12-24", "2023-12-26")
    print(usage_data)