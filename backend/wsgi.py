from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/submit', methods = ['POST'])
def submit():
    title = request.form['title']
    link = request.form['link']
    image_url = request.fomr['image_url']

    print(f'Title: {title}, Image URL: {image_url}, Link: {link}')
    return jsonify({"message": "Form submitted successfully!"}), 200

if __name__ == '__main__':
    app.run()