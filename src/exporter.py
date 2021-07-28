import argparse


from Get_Sensor_Data import SensorApiHandler
from  utils.date_utils import  get_current_time

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=str, help="Please enter the name of place/sensor")
    parser.add_argument("--duration", type=int, help="Please enter the time duration in seconds")
    parser.add_argument("--output", required=True, type=str, help="Please enter the path to save the CSV file")
    args = parser.parse_args()

    sensor_name= args.name
    duration = args.duration
    save_path = args.output
    current_time = get_current_time()

    sensorapi_handler = SensorApiHandler(sensor_name=sensor_name, duration=duration, save_path =save_path, current_time=current_time )
    print(sensor_name, duration, save_path)
    if not duration:
        sensorapi_handler.request_sensor_data()
    else:
        sensorapi_handler.request_sensor_data_between_time()