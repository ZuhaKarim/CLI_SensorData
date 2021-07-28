import os
import requests
import pandas as pd
from urllib3._collections import HTTPHeaderDict
import datetime

from utils.date_utils import get_current_time, add_current_time

class SensorApiHandler:

    def __init__(self, sensor_name:str, save_path:str, duration:int, 
                       current_time:str):
        """
        Initializing request handling parameters
        
        Arguments
        ---------
        sensor_name: string
            The name of sensor entered by user
        save_path: string
            Path name entered by user
        duration: int
            Duration of sensor reading entered by user
        current_time: int
            Current time in UTC 
        
        Returns
        ------
        None
        """
        self.sensor_name = sensor_name
        self.duration = duration
        self.save_path = save_path
        self.current_time = current_time

        localhost = 'http://localhost:8085'
        self.url = os.path.join(localhost,'data',self.sensor_name)

    def request_sensor_data_between_time(self):
        """
          Sending request with time duration(from - to)
        
        Arguments
        ---------
        None
        
        Returns
        -------
        None
        """
        updated_time = add_current_time(self.current_time, self.duration)
        payload = {'from': self.current_time.strftime("%Y-%m-%dT%H:%M:%SZ"), 
                   'to': updated_time.strftime("%Y-%m-%dT%H:%M:%SZ")}

        try:
            req = requests.get(self.url, params=payload)
            get_response = req.json()
            self.__process_json(get_response['data'])

        except requests.exceptions.HTTPError as e:
            print(e.response.text)

    def request_sensor_data(self):
        """
            Sending request with no duration

        Arguments
        ---------
        None

        Returns
        -------
        None
        """
        try:
            req = requests.get(self.url, params={})
            get_response = req.json()
            self.__process_json(get_response['data'])

        except requests.exceptions.HTTPError as e:
            print(e.response.text)


    def __process_json(self, data:str):
        """
        Extracts required data from json.

        Arguments
        ---------
        data: string
            Response data from API
        
        Returns
        -------
        None
        """
        final_results = {}
        final_time = []
        final_value = []
        for i in data:
            final_time.append(i['t'])
            final_value.append(i['vb'])
        final_result = {'Time' : final_time , 'Value' : final_value}
        self.__write_to_csv(final_result, self.save_path)


    def __write_to_csv(self, result:dict, file_path:str):
        """
        Saves result to a csv file.

        Arguments
        ---------
        result: dictionary
            Processed data for saving in CSV format
        file_path: string
            Path to save the file
        
        Returns
        -------
        None

        """
        df = pd.DataFrame(result)
        df.to_csv(file_path, index = False)
    


if __name__ == '__main__':
    sn = 'kitchen/lamp'
    d = 60
    out = './data.csv' 
    cur = get_current_time()
    sensor = SensorApiHandler(sensor_name=sn, duration=d, save_path=out, current_time=cur)
    sensor.request_sensor_data_between_time()
