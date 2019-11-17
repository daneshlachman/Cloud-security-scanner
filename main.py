import os
import hashlib
import time
from helpers.fileProcessor import readfile
import requests, json
import pdb


class Scanner:
    def __init__(self):
        self.FileToCompare = []
        self.HashToCompare = []
        self.error_files = []
        self.path = None
        self.interval = 10
        self.whitelist = []

    def start_scanning(self, path, interval, whitelist):
        self.path = path
        self.interval = interval
        self.whitelist = whitelist
        self.scan_directories()

    def scan_directories(self):
        files = []

        for r, d, f in os.walk(self.path):
            for file in f:
                if file in self.whitelist:
                    continue
                file_and_hash_obj = {}
                current_file = os.path.join(r, file)
                current_modified_date = os.path.getmtime(current_file)
                hash_content = (str(readfile(current_file)) + str(current_modified_date))
                file_and_hash_obj.update({"file": current_file})
                file_and_hash_obj.update({"hash": hashlib.md5(hash_content.encode('UTF-8')).digest()})
                files.append(file_and_hash_obj)
        send_data_to_logger(files)
        time.sleep(self.interval)
        self.scan_directories()


def send_data_to_logger(files):
    with open('config.json') as json_config:
        data = json.load(json_config)
        request_data = {
            "uuid": data['uuid'],
            "computer": data['computer_name'],
            "files": files
        }
    response = requests.post(url=data['logger_address'], data=data)
