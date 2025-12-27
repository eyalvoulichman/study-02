import os
import time
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Configure Redis connection from environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

# Initialize Redis client
cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"Hello World! I have been seen {count} times.\n"

@app.route('/health')
def health():
    try:
        cache.ping()
        return jsonify(status="UP", redis="CONNECTED"), 200
    except Exception as e:
        return jsonify(status="DOWN", redis=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
# Triggering CI pipeline


