import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=str, help="Please enter the name of place/sensor")
    parser.add_argument("--duration", type=int, help="Please enter the time duration in seconds")
    parser.add_argument("--output", required=True, type=str, help="Please enter the path to save the CSV file")
    args = parser.parse_args()

    User_sensor_name = args.name
    User_time_duration = str(args.duration)
    User_file_path = args.output