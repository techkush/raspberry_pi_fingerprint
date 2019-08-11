from flask import Flask, jsonify, json, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

# {"index" : 125}
@app.route('/form_example', methods=['POST'])
def form_example():

    if request.method == 'POST':
        req_data = request.get_json()
        index = req_data['index']
        print(index)
        return 'Index Number Sent!'


if __name__ == '__main__':
    app.run(debug=True)
