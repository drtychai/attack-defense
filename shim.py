from flask import Flask
from flask import jsonify
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def make_request(flag):
    url = 'http://monitor.ructfe.org/flags'
    headers = {'X-Team-Token: API_TOKEN'}
    response = requests.put(url, data=flag, headers=headers) 

    return response


@app.route('/get-targets')
def get_targets():
    target_list = []
    with open('targets.txt', 'r') as file:
        for target in file:
            target_list.append(target.strip('\n'))
    
    return jsonify(target_list)

        
@app.route('/submit-flag')
def submit_flag():
   """ Submit flags"""
   if request.method == 'POST':
       flag = request.args.get('flag')
       response = make_request(flag)

       return response['msg']

if __name__ == '__main__':
    app.run(debug=True)
