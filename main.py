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
print(json.dumps(live_data, indent=4))

