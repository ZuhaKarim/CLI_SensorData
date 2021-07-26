import argparse
import requests
import pandas as pd
import os
from argparse import ArgumentParser

class Get_Sensor_Data:

    def __init__(self):
        self.User_sensor_name = ''
        self.User_time_duration = ''
        self.User_file_path = ''
        self.final_result = {}


    #Taking user I/p
    def taking_user_ip(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--name", required=True, type=str, help="Please enter the name of place/sensor")
        parser.add_argument("--duration", required=True, type=int, help="Please enter the time duration in seconds")
        parser.add_argument("--output", required=True, type=str, help="Please enter the path to save the CSV file")
        args = parser.parse_args()

        self.User_sensor_name = args.name
        self.User_time_duration = str(args.duration)
        self.User_file_path = args.output
    

    # Sending req
    def sending_req(self):
        url = os.path.join('http://localhost:8085','data', self.User_sensor_name)
        Get_Req = requests.get(url)
        Get_Req_Response = Get_Req.json()

        final_time = []
        final_value = []
        for i in Get_Req_Response['data']:
            final_time.append(i['t'])
            final_value.append(i['vb'])
        self.final_result = {'time' : final_time , 'value' : final_value}
        return self.final_result
     

    #Writing to CSV
    def writing_to_csv(self):
        df = pd.DataFrame(self.final_result)
        df.to_csv(os.path.join(self.User_file_path,'data.csv'), index = False)
  
