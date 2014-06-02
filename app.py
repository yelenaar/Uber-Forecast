import datetime
import json

from flask import Flask
app = Flask(__name__)
INPUT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

@app.route('/<int:day_int>')
def hello(day_int):
	return json.dumps(day_int)

def brain_on(filename):
	with open(filename) as f:
		data = json.load()
	for index in range(len(data)):
		data[index] = utc_to_epoch(data[index])
	del data[:]

def utc_to_epoch(uat_timestamp):
	date.strptime)uat_timestamp, INPUT_TIMESTAMP_FORMAT).strftime('%s')

if __name__ == "__main__":
	app.run()