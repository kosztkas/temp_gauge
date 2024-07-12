from flask import Flask
from flask import render_template
import os
import requests
app = Flask(__name__)

api_key=os.environ["API_KEY"]
server_path = "http://10.0.0.10:8080/api/measurement/latest/location/szoba/type/"

@app.route('/')
def hello():
    URL_tmp = server_path+"temperature?api_key="+api_key
    URL_hmd = server_path+"humidity?api_key="+api_key
    r = requests.get(URL_tmp)
    r2 = requests.get(URL_hmd)
    t_data = r.json()
    h_data = r2.json()
    return render_template('temp.html', temp=str(t_data['value']), humid=str(h_data['value']), date=str(t_data['createdAt']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
