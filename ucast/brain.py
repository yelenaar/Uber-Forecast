from sklearn import svm
import datetime
import json
import pprint

INPUT_TIMERANGE_FORMAT = "%Y-%m-%d"
INPUT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

def brain_on():
	with open('../data/uber_demand_prediction_challenge.json') as f:
		data = json.load(f)
	for index in range(len(data)):
		data[index] = datetime.datetime.strptime(data[index], INPUT_TIMESTAMP_FORMAT)
	return data

def time_of_the_day():
	pass

def is_holiday():
	pass

def is_weekend():
	pass

class UberLogin(object):
	def __init__(self, date_point):
		self.timestamp = date_point.strftime('%s')
		self.time_of_the_day = date_point
		self.day_of_the_month = date_point.day
		self.day_of_the_week = date_point.weekday()
		self.month_of_the_year = date_point.month
		self.year = date_point.year
		self.is_holiday = date_point
		self.is_weekend = date_point

class Brain():
	def learn(datapoints):
		isinstance(datapoints)
		pass

	def forecast(timerange, model):
		pass

	def create_matrix(datapoints):
		pass

	def get_time_range(timerange):
		tr = timerange.split('TO')
		timerange_from = date.strptime(tr[0], INPUT_TIMERAGE_FORMAT).strftime('%s')
		timerange_to = date.strptime(tr[1], INPUT_TIMERAGE_FORMAT).strftime('%s')
		return [timerange_from, timerange_to]
