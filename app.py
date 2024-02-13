from flask import request, jsonify, Flask, redirect, make_response
import requests

import os

app = Flask(__name__)

# flask run --host 172.31.255.1 --port 5000
# http://127.0.0.1:5000

current_services = ['echo', 'register']
@app.route('/' , methods = ['GET', 'POST'])
def hello():
    output = 'Hello from API Entrypoint!'
    print('###################################')
    print(output)
    if validate()[1] != 200 :
        return 'Unauthorized'
    output = output + '\n' + 'currently we support those APIs:' + '\n' + '/v1/echo' + '\n' + '/v1/register'
    return output


# curl -i -H 'x-api-key: asoidewfoef' -H 'X-Original-IP: 127.0.0.1' http://127.0.0.1:5000
@app.route('/v1/validate', methods = ['GET', 'POST'])
def validate():
    if request.headers.get("X-Api-Key") == 'asoidewfoef': #os.getenv('X-Api-Key'):
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401



@app.route('/v1/echo', methods = ['GET', 'POST'] )
def redirect_echo_service():
    # return redirect_to("http://192.168.1.195:10030/")
    return make_get_request("http://192.168.1.195:10030/")


@app.route('/v1/register', methods = ['GET', 'POST'] )
def redirect_register_service():
    return make_get_request("http://192.168.1.195:10031/")
    


# def redirect_to(url):
#     if validate()[1] != 200 :
#         return 'Unauthorized'
#     original_ip = request.remote_addr
#     custom_headers = {'X-Original-IP': original_ip}
#     print('original_ip: ',original_ip)
#     return redirect(url, code=301)


def make_get_request(url):
    custom_headers = {'X-Original-IP': request.remote_addr}
    # custom_headers = {'X-Original-IP': '127.0.1.1'}
    response = requests.get(url, headers=custom_headers)
    print(response.status_code)
    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        return "GET request failed with status code: {}".format(response.status_code)

