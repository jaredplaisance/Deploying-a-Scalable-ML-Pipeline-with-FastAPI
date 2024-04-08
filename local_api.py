import json
import requests

# send a GET using the URL http://127.0.0.1:8000
url_get = "http://127.0.0.1:8000/"
r_get = requests.get(url_get)

# print the status code
print("GET request status code:", r_get.status_code)
# print the welcome message
print("Welcome message from GET request:", r_get.json())

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
url_post = "http://127.0.0.1:8000/data/"
r_post = requests.post(url_post, json=data)

# print the status code
print("\nPOST request status code:", r_post.status_code)
# print the result
print("Result from POST request:", r_post.json())
