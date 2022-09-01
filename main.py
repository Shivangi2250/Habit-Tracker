import requests
from datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

"""creating pixela account,Once created comment out the response"""
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

"""CREATING A GRAPH"""
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params={
    "id":"graph2",
    "name":"Cycling Graph",
    "unit":"km",
    "type": "float",
    "color": "ajisai"
}

headers = {                                 #creating header is like creating extreme secret password to prevent from
                                            # stealing our passwords
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(graph_response.text)

print(f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}.html")

"""POSTING VALUE ON GRAPH"""
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

today = datetime.now()
# today = datetime(year=2022,month=8,day=29)
# print(today.strftime("%Y%m%d"))

value_params={
    "date": today.strftime("%Y%m%d"),
    "quantity":"5"
}
value_response = requests.post(url=value_endpoint,json=value_params,headers=headers)
print(value_response.text)

"""UPDATING GRAPH"""
updated_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{value_params['date']}"


updated_params = {
    # "name": "updated graph",
    # "unit":"km",
    # "color":"momiji"
    "quantity":"2"


}
update_response = requests.put(url=updated_graph_endpoint,json=updated_params,headers=headers)
print(update_response.text)

"""DELETE GRAPH"""
# delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{value_params['date']}"
#
#
#
# # delete_response = requests.delete(url=delete_pixel,headers=headers)
# # print(delete_response.text)