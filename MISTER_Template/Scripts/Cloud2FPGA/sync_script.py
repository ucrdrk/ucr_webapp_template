
import requests
import json
import math
import os


def get_data(data_location):
    f = open(data_location,"r")
    return f.read()






global ip_addr 
ip_addr = get_data("ip_addr.txt")
global payload 
user_id = get_data("id_user.txt")
payload = {'value':user_id}


try:
    r = requests.get('http://'+ ip_addr +':8000/account/UserSync', params=payload) #getting account info

    if r.status_code == 200:
        server_variables = json.loads(r.text)
        print(server_variables)



except requests.exceptions.RequestException as e:
    raise SystemExit(e)