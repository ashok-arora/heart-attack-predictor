import requests
import json

url = "https://capstone-project-hap.herokuapp.com/predict"

payload = json.dumps({
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
    "thall": 1
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)