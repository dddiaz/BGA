Python flask app to retrieve Blood Glucose Values

For now we will pull DB data from a mongodb maintained by nightscout
In the future I would like to transition to pulling from Dexcom directly

This project requires a non version controlled file called AppSettings.ini
Inside there you should put your Nighscout MongoDB Connection String

ex.
[database]
db_connection_string: 'mongodb://xxx:yyy@zzz'

commands to run web app
docker build -t flask-sample-one:latest .
docker run -d -p 5000:5000 flask-sample-one

debug:
docker logs 0630eec34b08




# postman?