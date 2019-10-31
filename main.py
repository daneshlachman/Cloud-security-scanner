import os
import hashlib
from helpers.fileProcessor import readfile
import json, threading, pdb, datetime, time


class FileChange:
    def __init__(self, interval, whitelist, path):
        self.FileToCompare = []
        self.HashToCompare = []
        self.error_files = []
        self.path = path
        self.interval = interval
        self.whitelist = whitelist
        self.scan_directories()

    def scan_directories(self):
        files = []
        timeStampsLastModified = []
        hashes = []
        combinedPathAndHash = {}

        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                if file in self.whitelist:
                    continue
                currentFile = os.path.join(r, file)
                currentModifiedDate = os.path.getmtime(self.path)
                hashContent = (str(readfile(currentFile)) + str(currentModifiedDate))
                files.append(currentFile)
                hashes.append(hashlib.md5(hashContent.encode('utf-8')).digest())
        time.sleep(self.interval)

        # CHECK FOR HASHES TO BE IDENTICAL
        FileChange.change_detector(self, files, hashes)
        # DO SOMETHING RECURSIVE
        self.scan_directories()

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

# whitelistedFiles = ['randomtext.txt']
# interval = 3
# FileChange(interval, whitelistedFiles)
