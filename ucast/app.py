import json

from flask import Flask
app = Flask(__name__)

@app.route('/<int:day_int>')
def hello(day_int):
	return json.dumps(day_int)

if __name__ == "__main__":
	app.run()