import argparse
import requests
import pandas as pd
import os
from argparse import ArgumentParser
#./exporter --name=kitchen/lamp --duration=60 --output=/home/jane/data.csv 

#Taking user I/p
parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True, type=str, help="Please enter the name of place/sensor")
parser.add_argument("--duration", required=True, type=int, help="Please enter the time duration in seconds")
parser.add_argument("--output", required=True, type=str, help="Please enter the path to save the CSV file")
args = parser.parse_args()

User_sensor_name = args.name
User_time_duration = args.duration
User_file_path = args.output
print(User_sensor_name, User_time_duration, User_file_path)



# Sending req
url = 'http://localhost:8085/data/'+ User_sensor_name +'/'+ User_time_duration
print(url)
Get_Req = requests.get(url)
Get_Req_Respone = Get_Req.json()

final_time = []
final_value = []
for i in Get_Req_Respone['data']:
    final_time.append(i['t'])
    final_value.append(i['vb'])
final_result = {'time' : final_time , 'value' : final_value}

#Writing to CSV
df = pd.DataFrame(final_result)
df.to_csv('data.csv', index = False)
# csvFile = open('/home/zuhakarim/Work//data.csv', "w")

