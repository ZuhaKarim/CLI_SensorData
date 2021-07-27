import os
import requests
import pandas as pd
from urllib3._collections import HTTPHeaderDict
import datetime

from utils.date_utils import get_current_time, add_current_time

#./exporter --name=kitchen/lamp --duration=60 --output=/home/jane/data.csv 

class GetSensorData:

    def __init__(self, sensor_name:str, save_path:str, duration:int, 
                       current_time:str):
        """

        """
        self.sensor_name = sensor_name
        self.duration = duration
        self.save_path = save_path
        self.current_time = current_time

        localhost = 'http://localhost:8085'
        self.url = os.path.join(localhost,'data',self.sensor_name)

    def request_sensor_data_between_time(self):
        """

        """
        updated_time = add_current_time(self.current_time, self.duration)
        payload = {'from': self.current_time.strftime("%Y-%m-%dT%H:%M:%SZ"), 
                   'to': updated_time.strftime("%Y-%m-%dT%H:%M:%SZ")}

        try:
            req = requests.get(self.url, params=payload)
            print(req.url)
            get_response = req.json()
            self.__process_json(get_response['data'])

        except requests.exceptions.HTTPError as e:
            print(e.response.text)

    def request_sensor_data(self):
        """

        """
        try:
            req = requests.get(self.url, params={})
            get_response = req.json()
            self.__process_json(get_response['data'])

        except requests.exceptions.HTTPError as e:
            print(e.response.text)


    def __process_json(self, data:str):
        """
        Extracts required data from from json.
        """
        final_results = {}
        final_time = []
        final_value = []
        for i in data:
            final_time.append(i['t'])
            final_value.append(i['vb'])
        final_result = {'Time' : final_time , 'Value' : final_value}
        print(len(final_result['Time']))
        self.__write_to_csv(final_result, self.save_path)


    def __write_to_csv(self, result:dict, file_path:str):
        """
        Saves result to a csv file.
        """
        df = pd.DataFrame(result)
        df.to_csv(file_path, index = False)
    


if __name__ == '__main__':
    sn = 'kitchen/lamp'
    d = 60
    out = './data.csv' 
    cur = get_current_time()

    sensor = GetSensorData(sensor_name=sn, duration=d, save_path=out, current_time=cur)
    sensor.request_sensor_data_between_time()
