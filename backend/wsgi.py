import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from crud_interface_callback import get_crud_interface_callback

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    prompt = data.get('prompt')
    
    print("---------------------------------Prompt:---" + prompt)

    callback = get_crud_interface_callback(prompt)

    os.system(str(callback))

    print("---------------------------------Callback:---" + callback)
    
    return jsonify({"message": "Codebase Updated"})

    # print(f"Received prompt: {prompt}")

    # response_data = extract_context(prompt)
    
    # return jsonify({"message": response_data})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)