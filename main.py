import requests
import json

from defs import *
from utils import *

from requests_toolbelt.utils import dump
from secrets import API_TOKEN, CUSTOMER_ID, UTILITY_ID
from datetime import datetime

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID




    

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

