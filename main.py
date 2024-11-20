import requests
import json

from utils import get_service_points_list, get_live_data, get_displayed_data

from requests_toolbelt.utils import dump
from config import API_TOKEN, CUSTOMER_ID, UTILITY_ID
from datetime import datetime

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID


service_points_list = get_service_points_list(CUSTOMER_ID)

servicePointID = service_points_list['data']['servicePoints'][0]['servicePointId']

live_data = get_live_data(servicePointID)


displayed_data = get_displayed_data(live_data)

print("Current Power Flow:")
if 'solar' in displayed_data:
    print(f"  Solar ({displayed_data['solar']['name']}): {displayed_data['solar']['power']} kW")
if 'grid' in displayed_data:
    print(f"  Grid: {displayed_data['grid']} kW")
if 'home' in displayed_data:
    print(f"  Home: {displayed_data['home']} kW")    
if 'battery' in displayed_data:
    print(f"  Battery: {displayed_data['battery']['power']} kW")
    print(f"  Battery State of Charge: {displayed_data['battery']['stateOfCharge']}%")
if 'ev' in displayed_data:
    print(f"  EV: {displayed_data['ev']} kW")
