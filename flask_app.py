from flask import Flask, request
import requests
import json


def getCityFromIp(ip_address):
    response = requests.get('http://ip-api.com/json/{}'.format(ip_address))
    return json.loads(response.text).get('city')


def search_flights_to(source, destination):
    search_params = {
        'flyFrom': source,
        'to': destination,
        'dateFrom': '18/06/2017',
        'dateTo': '25/06/2017',
        'partner': 'picky'
    }

    response = requests.get("https://api.skypicker.com/flights", params=search_params)
    return json.loads(response.text).get('data')

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_ip = request.headers.get('X-Real-IP')  # request.remote_addr doesn't work on pythonanywhere

    source = getCityFromIp(user_ip)
    destination = request.args.get('destination', 'Minsk')

    out = "<html>Flights from {} to {}<ul>".format(source, destination)
    for flight in search_flights_to(source, destination)[:5]:
        out += "<li>{cityFrom} > {cityTo}; {price} EUR: <a href='{deep_link}'>book</a></li>".format(**flight)
    out += "</ul></html>"

    return out

