from flask import Flask, request, jsonify
from flask_cors import CORS 
from main import ContentManager

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173", "supports_credentials": True}})


@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/submit', methods = ['POST'])
def submit():
	data = request.form.to_dict()
	field = data.get('field', 'news')
	content_manager = ContentManager(field, data)
	file_path = content_manager.create_md_file()
	print(file_path)
	return jsonify({"message": "Markdown file created", "file_path": file_path})

if __name__ == '__main__':
	app.run()