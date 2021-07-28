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
The CLI application can be run using a single command:
  * With **3** parameters
    * The application expects 3 parameters:
      * name
      The name of the place and sensor for which data is required.
      * duration
      The time from which to which, the data is reequired.
      * output
      Path where the CSV file will be stored on your system.
      
  Type the following command in exporter folder on CLI:    
      '''python3 exporter.py --name kitchen/lamp --output /home/work/data.csv --duration 20'''
      
  * With **2** parameters
   * The application expects 2 parameters:
      * name
      The name of the place and sensor for which data is required.
      * output
      Path where the CSV file will be stored on your system.
  Type the following command in exporter folder on CLI:      
      **python3 exporter.py --name kitchen/lamp --output /home/work/data.csv **
 
 

