import requests
import json

def get_local_temp(lat, long):
    url = "http://localhost:5000/localweather"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Unable to locate user's geo-coordinates")

def get_local_city():
    url = 'http://api.ipstack.com/check?access_key=4e664fea892397e28b7c547522ac3f48'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Unable to locate user's geo-coordinates")


if __name__ == '__main__':
    pass
    # get_local_city()
