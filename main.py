import os
import hashlib
import time
from helpers.fileProcessor import readfile


class FileChange:
    def __init__(self):
        self.FileToCompare = []
        self.HashToCompare = []
        self.error_files = []
        self.path = None
        self.interval = None
        self.whitelist = None

    def start_scanning(self):
        self.scan_directories()

    def scan_directories(self):
        files = []
        hashes = []

        for root, directory, f in os.walk(self.path):
            for file in f:
                if file in self.whitelist:
                    continue
                current_file = os.path.join(root, file)
                current_modified_date = os.path.getmtime(self.path)
                hash_content = (str(readfile(current_file)) + str(current_modified_date))
                files.append(current_file)
                hashes.append(hashlib.md5(hash_content.encode('utf-8')).digest())
        time.sleep(self.interval)

        # CHECK FOR HASHES TO BE IDENTICAL
        FileChange.change_detector(self, files, hashes)
        self.scan_directories()

    # function for validating of hashes have changed, if so append corresponding file into error list
    def change_detector(self, files, hashes):
        if self.FileToCompare != [] and self.HashToCompare != []:
            i = 0
            for file, hash in zip(files, hashes):
                if file != self.FileToCompare[i] and hash != self.HashToCompare[i]:
                    self.error_files.append(self.FileToCompare[i])
                i += 1
        else:
            self.FileToCompare = files
            self.HashToCompare = hashes
        print(self.error_files)
