from flask import Flask
from flask import request
import json, pdb
from main import FileChange
from threading import Thread

# initiate app & scanner object
app = Flask(__name__)
scannerObject = FileChange()


# define route for config file from the logger
@app.route('/whitelist', methods=['POST'])
def process_whitelist_files():
    if request.method == 'POST':
        scannerObject.path = json.loads(request.form['path'])
        scannerObject.whitelist = json.loads(request.form['whitelist'])
        scannerObject.interval = json.loads(request.form['interval'])
        return scannerObject.__dict__


def run_the_app():
    app.run(debug=True, port=12345, threaded=True)


def run_the_scanner():
    scannerObject.start_scanning()


if __name__ == '__main__':
    Thread(target=run_the_app()).start()
    Thread(target=run_the_scanner()).start()
