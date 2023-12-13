import requests
import configuration
import data



def post_new_user(body):
    return requests.post(configuration.BASE_URL + configuration.MAIN_USER,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def post_new_client_kit(kit_body):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + "authToken"
    return requests.post(configuration.BASE_URL + configuration.MAIN_USER_KIT,
                         json=kit_body,
                         headers=headers_dict)
response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())