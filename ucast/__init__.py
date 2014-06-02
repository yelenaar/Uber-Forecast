__author__ = 'Yelena Wu (yelenamqwu@gmailcom)'

import datetime
import json
import pprint

INPUT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

def brain_on(filename):
	with open(filename) as f:
		data = json.load()
	for index in range(len(data)):
		data[index] = utc_to_epoch(data[index])
	del data[:]

def utc_to_epoch(uat_timestamp):
	date.strptime)uat_timestamp, INPUT_TIMESTAMP_FORMAT).strftime('%s')