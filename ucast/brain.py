from sklearn import svm
from collections import Counter
import datetime, json, numpy, scipy, random

INPUT_TIMERANGE_FORMAT = "%Y-%m-%d"
INPUT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H"
DST_START_2012 = datetime.datetime(2012, 3, 11)
DST_END_2012 = datetime.datetime(2012, 9, 4)

def brain_on():
	with open('../data/uber_demand_prediction_challenge.json') as f:
		data = json.load(f)
	for index in range(len(data)):
		data[index] = to_washington_dc_time(datetime.datetime.strptime(data[index].split(':')[0], INPUT_TIMESTAMP_FORMAT))
	login_dict = Counter(data)
	return Logins(login_dict)

def to_washington_dc_time(dpoint): 
	if dpoint >= DST_START_2012 and dpoint < DST_END_2012:
		time_in_dc = dpoint + datetime.timedelta(hours = -4)
	else:
		time_in_dc = dpoint + datetime.timedelta(hours = -3)
	return time_in_dc

# download sunrise and sunset time table to determine day and night
def is_night(dpoint):
	if dpoint.hour > 5 and dpoint.hour < 19:
		return 0
	return 1

def is_weekend(dpoint):
	if dpoint.day < 5:
		return 1
	return 0

def is_rushhour(dpoint):
	if dpoint.hour < 10 and dpoint.hour >= 6 or dpoint.hour < 19 and dpoint.hour >= 16:
		return 1
	return 0

class Logins(list):
	def __init__(self, data_points):
		for item in data_points:
			self.append(UberLogin(item, data_points[item]))
		self.timestamp_max = max(data_points.keys())
		self.timestamp_min = min(data_points.keys())
		self.attributes_size = len(self[0].__dict__)

class UberLogin(object):
	def __init__(self, date_point, num):
		self.timestamp = int(date_point.strftime('%s'))
		self.hour_of_the_day = date_point.hour
		self.is_rushhour = is_rushhour(date_point)
		self.is_night = is_night(date_point)
		self.day_of_the_month = date_point.day
		self.day_of_the_week = date_point.weekday()
		self.is_weekend = is_weekend(date_point)
		self.number_of_logins_this_hour = num

	def learning_params(self):
		return [self.hour_of_the_day, self.day_of_the_week, self.day_of_the_month, self.is_rushhour, self.is_night, self.is_weekend]

class Brain(object):
	def __init__(self, login_points):
		if not isinstance(login_points, Logins):
			raise TypeError('login_points should be of Logins type!')
		if len(login_points) == 0:
			raise Exception('The brain needs more than 0 data points to learn. ENTER SOME DATA!')
		self.datapoints = login_points
		self.model = self.learn(login_points)

	def learn(self, login_points):
		if not isinstance(login_points, list):
			raise TypeError('Brain.learn only takes array objects.')
		X, y = self.create_matrices(login_points)
		clf = svm.SVR()
		clf.fit(X, y)
		return clf

	def forecast(self, timerange):
		# assuming input timerange are in washington dc timestamp format
		start_time, end_time = self.get_time_range(timerange)
		predicting_X = []
		predicted_timestamps = []
		for index in range(start_time, end_time+1, 3600):
			predicting_X.append(UberLogin(datetime.datetime.fromtimestamp(index), 0).learning_params())
		predicting_y = self.model.predict(predicting_X)
		return predicting_y

	def create_matrices(self, login_points):
		X = []
		Y = []
		timestamps = map(lambda x: x.timestamp, login_points)
		login_points.timestamp_max - login_points.timestamp_min
		for ts in range(int(login_points.timestamp_min.strftime('%s')), int(login_points.timestamp_max.strftime('%s')) + 1, 3600):
			if ts in timestamps:
				index = timestamps.index(ts)
				X.append(login_points[index].learning_params())
				Y.append(login_points[index].number_of_logins_this_hour)
				login_points.pop(index)
				timestamps.pop(index)
			else:
				new_login = UberLogin(datetime.datetime.fromtimestamp(index), 0) 
				X.append(new_login.learning_params())
				Y.append(new_login.number_of_logins_this_hour)
		return [X, Y]

	def get_time_range(self, timerange):
		tr = timerange.split('TO')
		timerange_from = int(tr[0])
		timerange_to = int(tr[1])
		return [timerange_from, timerange_to]
