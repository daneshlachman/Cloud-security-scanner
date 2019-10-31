from flask import Flask
from flask import request
import json
import pdb
from main import FileChange

app = Flask(__name__)

whitelistedFiles = ['randomtext.txt']
interval = 3
path = r"C:\Users\Danesh\Documents\Pythontestfolder"


@app.route('/whitelist', methods=['POST'])
def process_whitelist_files():
    if request.method == 'POST':
        # print(request.form['files'])
        print(json.loads(request.form['files']))
        pdb.set_trace()
        FileChange(interval, whitelistedFiles, path)
        return 'OK'


if __name__ == '__main__':
    app.run(debug=True, port=12345)  # run app in debug mode on port 5000
