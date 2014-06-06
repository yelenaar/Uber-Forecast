from sklearn import svm
import datetime
import json
import pprint

INPUT_TIMERANGE_FORMAT = "%Y-%m-%d"
INPUT_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"
DST_START_2012 = datetime.datetime(2012, 3, 11)
DST_END_2012 = datetime.datetime(2012, 9, 4)

def brain_on():
	with open('../data/uber_demand_prediction_challenge.json') as f:
		data = json.load(f)
	for index in range(len(data)):
		data[index] = to_washington_dc_time(datetime.datetime.strptime(data[index], INPUT_TIMESTAMP_FORMAT))
	# brain_cell = Brain(Logins(data))
	return Logins(data)

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

# download holiday calendar in dc to determine day and night
def is_holiday(dpoint):
	time_in_dc = to_washington_dc_time(dpoint)
	pass

def is_weekend(dpoint):
	if dpoint.day < 5:
		return 1
	return 0

# where generates fake data
def login_generator():
	if random.random() >= 0.5:
		return datetime.datetime.now()

class Logins(list):
	def __init__(self, data_points):
		for point in data_points:
			self.append(UberLogin(point))
		self.timestamp_max = max(data_points)
		self.timestamp_min = min(data_points)
		self.attributes_size = len(self[0].__dict__)

class UberLogin(object):
	def __init__(self, date_point):
		self.timestamp = int(date_point.strftime('%s'))
		self.is_night = is_night(date_point)
		self.day_of_the_month = date_point.day
		self.day_of_the_week = date_point.weekday()
		self.month_of_the_year = date_point.month
		# self.year = date_point.year
		# self.is_holiday = is_holiday(date_point)
		self.is_weekend = is_weekend(date_point)

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
		clf = svm.SVC()
		clf.fit(X, y)
		return clf

	def forecast(self, timerange):
		# assuming input timerange are in washington dc timestamp format
		start_time, end_time = self.get_time_range(timerange)
		predicting_X = []
		predicted_timestamps = []
		for index in range(start_time, end_time):
			predicting_X.append(UberLogin(datetime.datetime.fromtimestamp(index)).__dict__.values())
		predicting_y = self.model.predict(predicting_X)
		return predicting_y

	def create_matrices(self, login_points):
		X = []
		Y = []
		for index in range(int(login_points.timestamp_min.strftime('%s')), int(login_points.timestamp_max.strftime('%s'))):
			if index < login_points[0].timestamp:
				X.append(UberLogin(datetime.datetime.fromtimestamp(index)).__dict__.values())
				Y.append(0)
			elif index == login_points[0].timestamp:
				X.append(login_points[0].__dict__.values())
				Y.append(1)
				login_points.pop(0)
		return [X, Y]

	def get_time_range(self, timerange):
		tr = timerange.split('TO')
		timerange_from = int(tr[0])
		timerange_to = int(tr[1])
		return [timerange_from, timerange_to]
