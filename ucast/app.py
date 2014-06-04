import json
import datetime
import brain

from flask import Flask
app = Flask(__name__)
globdata = []

@app.before_first_request
def initializer():
	globdata = brain_on()

@app.route('/')
def hello():
	print "hello"
	return json.dumps("Hello, say something!")

@app.route('/range/<string:timerange>')
def execute_brain(timerange):
	Brain.learn(globdata)
	return json.dumps(timerange)

if __name__ == "__main__":
	app.run()