from flask import Flask
import time

api = Flask(__name__) # api

@api.route("/time")
def get_current_time():
    return {'time': time.time()}

