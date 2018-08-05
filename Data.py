import requests
import json

cities = {}
temp_is_hot = True


def update_weather():
    cities['local'] = update_local_weather()
    cities['hightemp'] = update_city('hightemp')
    cities['lowtemp'] = update_city('lowtemp')
    cities['highhumid'] = update_city('highhumid')
    cities['lowhumid'] = update_city('lowhumid')
    cities['heat'] = update_city('heat')
    cities['chill'] = update_city('chill')


def update_local_weather():
    local = get_local_city()
    lat = local['latitude']
    long = local['longitude']
    url = "http://localhost:5000/localweather"
    response = requests.post(url, json={'lat': lat, 'long': long})
    if response.status_code == 200:
        weather = json.loads(response.content.decode('utf-8'))
        weather['name'] = local['city']
        weather['state'] = local['region_code']
        return weather
    else:
        return False


def update_city(category):
    url = 'http://localhost:5000/singleweather/' + category
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        city = json.loads(response.content.decode('utf-8'))
        return city
    else:
        return False


def get_local_city():
    url = 'http://api.ipstack.com/check?access_key=4e664fea892397e28b7c547522ac3f48'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        city = json.loads(response.content.decode('utf-8'))
        return city
    else:
        return False


def get_city(category):
    return {
        'local': cities['local'],
        'hightemp': cities['hightemp'],
        'lowtemp': cities['lowtemp'],
        'highhumid': cities['highhumid'],
        'lowhumid': cities['lowhumid']
    }.get(category, {'response': cities['local']})


def switch_temp():
    global temp_is_hot
    temp_is_hot = not temp_is_hot

    if temp_is_hot:
        return cities['hightemp']
    else:
        return cities['lowtemp']


if __name__ == '__main__':
    pass
