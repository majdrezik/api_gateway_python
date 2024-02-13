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

### Notice what will happen when we choose to hit the /v1/register API - It'll get the micro-service that's running on a totally different url
![Screenshot 2024-02-13 at 3 06 38](https://github.com/majdrezik/api_gateway_python/assets/39953455/61dad2d4-4060-490d-ac51-419059d7326f)


### Here's the Entrypoint of the API_GATEWAY where we can see the active APIs
![Screenshot 2024-02-13 at 3 07 45](https://github.com/majdrezik/api_gateway_python/assets/39953455/5e35c3ff-d3a5-40df-84e3-633190f0d6b7)


### Notice what will happen when we choose to hit the /v1/echo API - It'll get the micro-service that's running on a totally different url
![Screenshot 2024-02-13 at 3 06 59](https://github.com/majdrezik/api_gateway_python/assets/39953455/4bd80d78-68cc-4ac8-b12a-d9eaf703ae9d)

### When we try to access the micro-service directly, the request will be blocked. in real life this will be handled via FIREWALL or other ways, here I created a DUMMY firewall with ALLOWED LIST that only clients coming from API_GATEWAY can access (original url)
![Screenshot 2024-02-13 at 3 07 18](https://github.com/majdrezik/api_gateway_python/assets/39953455/7a0894dd-0106-4c1f-bb19-22f2057ac077)

