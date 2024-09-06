from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/submit', methods = ['POST'])
def submit():
    title = request.form['title']
    link = request.form['link']
    image_url = request.fomr['image_url']

    print(f'Title: {title}, Image URL: {image_url}, Link: {link}')
    return 'Submit'

if __name__ == '__main__':
    app.run()