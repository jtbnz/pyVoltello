import requests
import json

from utils import get_service_points_list, get_service_points_detail, get_live_data, get_service_points_der, get_service_points_usage

from requests_toolbelt.utils import dump
from secrets import API_TOKEN, CUSTOMER_ID, UTILITY_ID
from datetime import datetime

customer_id = CUSTOMER_ID
utility_id = UTILITY_ID


service_points_list = get_service_points_list(CUSTOMER_ID)

servicePointID = service_points_list['data']['servicePoints'][0]['servicePointId']

live_data = get_live_data(servicePointID)


displayed_data = get_displayed_data(live_data)

print("Current Power Flow:")
if 'solar' in displayed_data:
    print(f"  Solar ({displayed_data['solar']['name']}): {displayed_data['solar']['power']} W")
if 'grid' in displayed_data:
    print(f"  Grid: {displayed_data['grid']} W")
if 'battery' in displayed_data:
    print(f"  Battery: {displayed_data['battery']['power']} W")
    print(f"  Battery State of Charge: {displayed_data['battery']['stateOfCharge']}%")
if 'home' in displayed_data:
    print(f"  Home: {displayed_data['home']} W")
if 'ev' in displayed_data:
    print(f"  EV: {displayed_data['ev']} W")
