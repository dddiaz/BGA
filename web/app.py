import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import configparser
from bson.json_util import dumps
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
MONGO_DB = config['nightscout-mongodb']['MONGO_DB']
### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
MONGODB_URI = ''.join(['mongodb://', MONGO_USER, ':', MONGO_USER_PASSWORD,
                        '@', MONGO_HOST, ':', str(MONGO_PORT), '/', MONGO_DB])

#print(MONGODB_URI)
client = MongoClient(MONGODB_URI)

db = client.get_default_database()

entries = db['entries']


@app.route('/')
def hello_world():
    return 'BGA Web API'


@app.route('/lastbg')
def lastbg():
    if entries is not None:
        #cursor = entries.find().sort([("date", -1)]).limit(1)
        cursor = entries.find().sort([("date", -1)]).limit(1)
        # todo check database is set up and connected to
        # also what happens if no values in db
        # TODO change this to not put json in list, just return single
        # Hack to get around bson dumping json into json array instead of single object
        # telegraf doesnt like [{json}]

        #temp = dumps(cursor)
        #data = json.loads(temp)
        #return json.dumps(data[0])

        return dumps(cursor)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
