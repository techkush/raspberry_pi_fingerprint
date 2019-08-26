from flask import Flask, jsonify, json, request

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

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
        sensor(index)
        # return 'Index Number Sent!'


def sensor(index):
    f = in_sensor()
    try:
        print('Waiting for finger...')
        while (f.readImage() == False):
            pass
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if (positionNumber == -1):
            print('No match found!')

        mark_att(week, subject, lec_name, "--- No student ---")

        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
        f.loadTemplate(positionNumber, 0x01)
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        print('SHA-2 hash of template: ' +
              hashlib.sha256(characterics).hexdigest())

        payloads = {'method': 3, 'fingprint': hashlib.sha256(
            characterics).hexdigest(), 'index': index}
        r = requests.post('http://192.168.1.8:3000', json=payloads)

        req_text = r.text
        data = json.loads(req_text)

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))


# Initialize Sensor
def in_sensor():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if (f.verifyPassword() == False):
            raise ValueError('The given fingerprint sensor password is wrong!')
        return f
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    print('Currently used templates: ' + str(f.getTemplateCount()) +
          '/' + str(f.getStorageCapacity()))


if __name__ == '__main__':
    app.run(debug=True)
