from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173", "supports_credentials": True}})


@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/submit', methods = ['POST'])
def submit():
	data = request.form.to_dict()
	print(data)
	return "done"

if __name__ == '__main__':
	app.run()