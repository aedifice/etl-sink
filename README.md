# ETL Sink Service

This is not meant as a standalone service. Rather, it acts as an example data sink to pair with the [etl-service](https://github.com/aedifice/etl-service) for demo and testing purposes.

Whenever a command is run through etl-service, it sends its results here. This service will then store and be able to retrieve results for future perusal.

## Using the service

**Running the service**

This service encapsulates its requirements in a Docker container. So, while you don't need to install Python requirements directly, you at least need to be able to run [Docker](https://www.docker.com/) commands.

To build the Docker image, execute:
`./build-container.sh`

To start a container based on the image, execute:
`./run-container.sh`

Alternatively, you can copy the Docker commands from the Shell scripts and run them from the Dockerfile's base directory.

Starting the container will start up the web service on `127.0.0.1:3514`

**Using the service's endpoints**

This service's endpoints mimic those in etl-service. There is a "Help" endpoint to list out current data files:
```
GET localhost:3514/help
```

And there is a "Manage Data" path for storing and retrieving data. The etl-service uses the POST action with this path to send data over for storage:
```
POST localhost:3514/etl/data_filename
```

The service saves the JSON body provided with the post to a new file (or overwrites an existing file with the same name, as provided by "data_filename"). This also makes use of Docker volumes to persist the data.

For example, the `web_example.json.template` file provided in the data directory matches what the web_example dropin command in etl-service would create.

The corresponding GET action will return the saved JSON.
```
GET localhost:3514/etl/data_filename
```
