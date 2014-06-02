__author__ = 'Yelena Wu (yelenamqwu@gmailcom)'

import datetime
import json
import pprint

INPUT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

def brain_on():
	with open('../data/uber_demand_prediction_challenge.json') as f:
		data = json.load(f)
	return data

def utc_to_epoch(uat_timestamp):
	date.strptime(uat_timestamp, INPUT_TIMESTAMP_FORMAT).strftime('%s')
