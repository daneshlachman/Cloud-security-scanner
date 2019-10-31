from flask import Flask
from flask import request
import json, pdb
from main import Scanner
from threading import Thread

# initiate app & scanner object
app = Flask(__name__)
Scanner = Scanner()


# define route for config file from the logger
@app.route('/whitelist', methods=['POST'])
def process_whitelist_files():
    if request.method == 'POST':
        Scanner.path = json.loads(request.form['path'])
        Scanner.whitelist = json.loads(request.form['whitelist'])
        Scanner.interval = json.loads(request.form['interval'])
        return Scanner.__dict__


def run_the_app():
    app.run(debug=True, port=12345, threaded=True)


def run_the_scanner():
    Scanner.start_scanning()


if __name__ == '__main__':
    Thread(target=run_the_app()).start()
    Thread(target=run_the_scanner()).start()
