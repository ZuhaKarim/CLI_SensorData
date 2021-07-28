# CLI_SensorData

### Introduction
This is a CLI application designed to get sensor data. It sends an API request to the server, fetches the response data and saves the time and value in a CSV file, to the path provided by user.

### Design Details
 * This application consists of:
    * separate class for handling API
    * separate util files
 * Separate classes help in scalability and to generalize the code.
 * Having separate functionality makes unit testing easier.
 * Doc strings are added for better documentation

### How to run

Use the following command to clone the application:    
```
git clone https://github.com/ZuhaKarim/CLI_SensorData
cd CLI_SensorData/src

```

The CLI application has the following arguments:
* The application expects 3 parameters:
  
  * name:
  The name of the place and sensor for which data is required.
   * duration:
   The time from which to which, the data is required.
   * output:
   Path where the CSV file will be stored on your system.
      
It can run in two modes:
#### Get all the data
 * With 2 parameters
   It expects --name and --output. Use following command to run it in this mode:
   ```
   python3 exporter.py --name kitchen/lamp --output /home/work/data.csv
   
   ```
#### Get data with time limit
 * With 3 parameters
   It expects --name, --duration and --output. Use following command to run it in this mode:
```
   python3 exporter.py --name kitchen/lamp --duration 20 --output /home/work/data.csv 

```
### Refrences
https://github.com/linksmart/historical-datastore
https://docs.python.org/3/library/
 
 

