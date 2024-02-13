from flask import Flask,request, jsonify

app = Flask(__name__)

ALLOWED_IP='127.0.0.1'

@app.route('/')
def hello():

    original_ip = request.headers.get('X-Original-IP')
    if original_ip is None or original_ip != ALLOWED_IP:
        return jsonify({'message': 'Error: This service cannot be accessed directly'}), 400

    
    output = 'Hello from ECHO server! running on http://192.168.1.195:10030/'
    print('\n###################################')
    print(output)
    print('###################################')
    return output, 200

# flask run --host 192.168.1.195 --port 10030 
# http://192.168.1.195:10030/

if __name__ == '__main__':
    print("echo server started running")
    