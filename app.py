import json
import os
import pdb
from threading import Thread

from flask import Flask

from main import Scanner

# initiate app & scanner object
# app = Flask(__name__)
Scanner_object = Scanner()


# define route for config file from the logger
# @app.route('/config', methods=['POST'])
# def process_whitelist_files():
#     if request.method == 'POST':
#         Scanner.path = json.loads(request.form['path'])
#         Scanner.whitelist = json.loads(request.form['whitelist'])
#         Scanner.interval = json.loads(request.form['interval'])
#         return Scanner.__dict__


def create_standard_config():
    pdb.set_trace()
    config = {
        'interval': '30',
        'path': r'C:\Users\DaneshLachman\Documents',
        'whitelist': [],
        'default_logger_ip': '192.168.123.123'
    }
    print('Creating config file with the following data: ', config)

    with open('config.json', 'w') as json_object:
        json.dump(config, json_object)


def run_the_scanner():
    if os.path.exists('config.json'):
        with open('config.json') as json_file:
            data = json.load(json_file)
        Scanner_object.start_scanning(data['path'], data['interval'], data['whitelist'])
    elif not os.path.exists('config.json'):
        create_standard_config()
        with open('config.json') as json_file:
            data = json.load(json_file)
        Scanner_object.start_scanning(data['path'], data['interval'], data['whitelist'])
    else:
        raise Exception('Error with finding/creating config file')


if __name__ == '__main__':
    Thread(target=run_the_scanner()).start()
