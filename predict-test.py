import requests
import json

flask_url = "127.0.0.1:6000"
docker_url = "127.0.0.1:7000"
heroku_url = "https://midterm-project-spotify.herokuapp.com/predict"

patient = {
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trtbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalachh": 150,
    "exng": 0,
    "oldpeak": 2.3,
    "slp": 0,
    "caa": 0,
    "thall": 14
}

print(requests.post(heroku_url, json=song).json())
