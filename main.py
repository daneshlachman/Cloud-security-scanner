import os
import hashlib
from fileProcessing import readfile

# path = input("Enter the to be scanned path ")
path = r"C:\Users\Danesh\Documents\Pythontestfolder"

files = []
timeStampsLastModified = []
hashes = []
whitelistedFiles = ['randomtext.txt']

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file in whitelistedFiles:
            continue
        currentFile = os.path.join(r, file)
        currentModifiedDate = os.path.getmtime(path)
        files.append(currentFile)
        timeStampsLastModified.append(currentModifiedDate)
        hashContent = (str(readfile(currentFile)) + str(currentModifiedDate))
        hashes.append(hashlib.md5(hashContent.encode('utf-8')))

# print all hashes of files in entererd path recursively
# for hash in hashes:
#     print(hash)


for x in files:
    print(x)

print('\n')

print('Number of files: ', len(files))
print('Number of timestamps: ', len(timeStampsLastModified))
print('Number of hashes: ', len(hashes))
