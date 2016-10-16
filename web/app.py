import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import configparser
import json

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('AppSettings.ini')

# gosh darn python 2.7
if 'nightscout-mongodb' not in config:
    print("Hey you forgot to setup your mongo db. check out the readme")

MONGO_USER = config['nightscout-mongodb']['MONGO_USER']
MONGO_USER_PASSWORD = config['nightscout-mongodb']['MONGO_USER_PASSWORD']
MONGO_HOST = config['nightscout-mongodb']['MONGO_HOST']
MONGO_PORT = config['nightscout-mongodb']['MONGO_PORT']
MONGO_PORT = config.getint('nightscout-mongodb', 'MONGO_PORT')
MONGO_DB = config['nightscout-mongodb']['MONGO_DB']
### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
MONGODB_URI = ''.join(['mongodb://', 'MONGO_USER', ':', 'MONGO_USER_PASSWORD',
                        '@', 'MONGO_HOST', ':', str(MONGO_PORT), '/', MONGO_DB])
# MONGODB_URI = 'mongodb://' + MONGO_USER + ':' + MONGO_USER_PASSWORD + '@' + MONGO_HOST \
#               + ':' + MONGO_PORT + '/' + MONGO_DB

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
print(MONGODB_URI)
client = MongoClient(MONGODB_URI)
# BG db is labled entries
bg = client.entries


@app.route('/')
def hello_world():
    return 'Flask Dockerized'


@app.route('/lastbg')
def lastbg():
    if client is not None:
        doc = bg.find().limit(1).sort({'$natural':-1})
        # to do check database is set up
        if doc is not None:
            return json.dumps(doc, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
