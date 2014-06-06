import multiprocessing
import Queue
import random
import datetime
import time

class DummyRobot(object):
	def __init__(self):
		self.proc = multiprocessing.Process(target=self.login_generator)
		
	def start(self):
		self.proc.start()

	def stop(self):
		self.proc.terminate()

	def login_generator(self):
		time.sleep(1.5)
		if random.random() >= 0.5:
			print datetime.datetime.now()
		print 0