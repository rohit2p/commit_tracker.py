import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "YOUR TOKEN"
USERNAME = "YOUR USERNAME"
ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Reading Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}
header = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
date = datetime.now()

pixel_endpoint = f"{graph_endpoint}/{ID}"

pixel_config = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many commits you did today: ")
}
response = requests.post(url=pixel_endpoint, headers=header, json=pixel_config)
print(response.text)
