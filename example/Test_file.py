import sys
import os
sys.path.append(os.path.abspath('..'))
from src.Get_Sensor_Data import Get_Sensor_Data

Exporting_Sensor_Data = Get_Sensor_Data()
Exporting_Sensor_Data.taking_user_ip()
Exporting_Sensor_Data.sending_req()
Exporting_Sensor_Data.writing_to_csv()
Exporting_Sensor_Data.get_date()