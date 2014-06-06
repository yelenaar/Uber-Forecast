import json
import datetime
import brain
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello():
	return json.dumps("Hello, say something!")

@app.route('/range/<string:timerange>.csv')
def execute_brain_to_csv(timerange):
	def generate():
		data = brain.brain_on()
		current_model = brain.Brain(data)
		login_stats = current_model.forecast(timerange)
		for row in login_stats:
			yield row + '\n'
	return Response(generate(), mimetype='text/csv')

if __name__ == "__main__":
	app.run()