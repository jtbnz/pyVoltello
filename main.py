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
#print(json.dumps(live_data, indent=4))

solar_now = live_data['data']['flowData']['power']['solar']['power']
solar_name = live_data['data']['flowData']['power']['solar']['nickName']
grid_now = live_data['data']['flowData']['power']['grid']['power']
battery_now = live_data['data']['flowData']['power']['battery']['power']
battery_charge_now = live_data['data']['flowData']['power']['battery']['stateOfCharge']
ev_now = live_data['data']['flowData']['power']['ev']['power']
home_now = live_data['data']['flowData']['power']['home']['power']

print(f"Current Power Flow for {solar_name}:")
print(f"  Solar: {solar_now} W")
print(f"  Grid: {grid_now} W")
print(f"  Battery: {battery_now} W")
print(f"  Battery State of Charge: {battery_charge_now}%")
print(f"  EV: {ev_now} W")
print(f"  Home: {home_now} W")
