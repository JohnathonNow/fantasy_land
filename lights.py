#!/usr/bin/env python3
import requests
import json
import os

token = os.environ["LIFX_API_KEY"]
print(token)

headers = {
    "Authorization": "Bearer {}".format(token),
}

def set():
    payload = {
      "states": [{
            "selector": "all",
            "hue": 200,
            "brightness": 1,
            "power": "on"
        }],
        "defaults": {
            "power": "off",
            "saturation": 0,
            "duration": 20.0 
        }
    }
    response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)

def hurt():
    payload = {
        "cycles": 1,
        "period": 0.25,
        "color": "red",
    }
    response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', data=json.dumps(payload), headers=headers)

hurt()
