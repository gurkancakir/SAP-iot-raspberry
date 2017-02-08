"""
    Gurkan Mustafa CAKIR
    08.02.2016
    HANA Cloud iot application for iot devices
"""
import requests
import time
import json

headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ef4a8a6ac52eb17e6eaf36e0ffd386'}
messageType = "c7f45d066b89cd3286d6"
deviceId = "cf99387b-f062-41c5-aae1-6cf66d4a8626"
url = "https://iotmmsp1942263232trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/"+deviceId
temp = 15
data = {
    "mode":"sync",
    "messageType":messageType,
    "messages":[
        {
        "sicaklik":temp,
        "timestamp": int(time.time())
        }
    ]
}
r = requests.post(url, data=json.dumps(data), headers=headers)
print r.status_code
