# MSSQL docker container

This branch contains a docker container for running MSSQL, which exposes the connection port so that local connections can be made to it. Follow the below steps to use it. This guide assumes you have docker installed and running:
https://www.docker.com/products/docker-desktop

#### Step 1:
Clone this repo and checkout this branch

#### Step 2:
Move the `docker-compose.yml` file to where ever your python application files are

#### Step 3:
Run `docker-compose up` from that folder on the command line

#### Step 4:
Wait until the command is finished

#### Step 5:
There is no step 5, your done.

#### Step 6:
You probably need to know how to connect to it? Details below:

##### From a GUI:

Host: `localhost`  
Port: `1433`  
Auth: `SQL Server Auth` (default)  
Login/User: `sa`  
Password: `Password123`  

##### From python:
```python
conn = pyodbc.connect(
    server="localhost",
    database="Your database name",
    user='sa',
    tds_version='7.4',
    password="Password123",
    port=1433,
    driver='/usr/local/lib/libtdsodbc.so' # check this driver exists
)
```
