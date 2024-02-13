# API Gateway Python Project

This project serves as an API Gateway implemented in Python using Flask.

## Description

The API Gateway is responsible for routing incoming requests to the appropriate backend services, managing authentication and authorization, and aggregating the responses before sending them back to the client.

## Features

- **Routing**: Directs incoming requests to the appropriate backend service based on the request path.
- **Authentication and Authorization**: Implements authentication and authorization mechanisms to ensure secure access to backend services.
- **Request Aggregation**: Aggregates responses from multiple backend services and sends a single response back to the client.
- **Logging**: Records request and response information for monitoring and debugging purposes.

## Installation

1. Clone the repository:
  ``` 
  git clone https://github.com/majdrezik/api_gateway_python.git
  cd api_gateway_python
```
3. Install dependencies:
```
  pip install -r requirements.txt
```

## Usage

1. Run the main Flask application: (root directory)
   
  ```flask run --host 172.31.255.1 --port 5000```

3. Run the services:
   - ```cd services/{SERVICE_NAME_1}```
     
   - ```flask run --host 192.168.1.195 --port 10030```

   - ```cd services/{SERVICE_NAME_2}```
   - ```flask run --host 192.168.1.195 --port 10031```
     
_Make sure you assing different ports to each service_

On `Postman` navigate to `http://127.0.0.1:5000` which acts as our Entrypoint (client) and choose different apis from the list (e.g `http://127.0.0.1:5000/v1/echo`)
This will show the starting point and the end result (starting from one url and ending in another url).
You can try accessing the micro-service directly, like `http://192.168.1.195:10030/` . this will fail (made a simple firewall)
