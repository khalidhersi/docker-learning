from flask import Flask
import redis

app = Flask(__name__)

# Retry connecting to Redis until it's ready

r = redis.Redis(host='redis', port=6379, decode_responses=True)



@app.route('/')
def hello_world():
    return 'Welocme to the count docker project'

@app.route('/count')
def counter():
    # Increment the 'visits' key
    visits = r.incr('visits')
    return f'Hello again! You have visited this page {visits} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)