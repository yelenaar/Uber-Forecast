import json
import datetime

import brain

from flask import Flask
app = Flask(__name__)

@app.before_first_request
def initializer():
	data = brain.brain_on()
	current_model = brain.Brain(data)

@app.route('/')
def hello():
	print "hello"
	return json.dumps("Hello, say something!")

@app.route('/range/<string:timerange>')
def execute_brain(timerange):
	core_system = Brain(globdata)
	timestamps = core_system.forecast(timerange)
	return json.dumps(timestamps)

if __name__ == "__main__":
	app.run()