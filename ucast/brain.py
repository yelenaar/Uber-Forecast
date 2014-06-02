from sklearn import svm
import datetime

INPUT_TIMERANGE_FORMAT = "%Y-%m-%d"

class UberLogin(object):
	def __init__(self, date_point):
		self.timestamp = date_point
		self.time_of_the_day = time_of_the_day(data_point)
		self.day_of_the_month = date_point.day
		self.day_of_the_week = date_point.weekday()
		# self.month_of_the_year = date_point.month
		# self.year = date_point.year
		self.is_holiday = is_holiday(date_point)
		self.is_weekend = is_weekend(date_point)

	def time_of_the_day(dpoint):
		pass

	def is_holiday(dpoint):
		return dpoint

	def is_weekend(dpoint):
		return dpoint.weekday() > 4

class Brain():
	def learn(datapoints):
		print datapoints
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
