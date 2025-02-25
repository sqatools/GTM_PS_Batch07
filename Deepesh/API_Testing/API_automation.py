import requests
import json
from pprint import pprint


def get_method_response():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.text)


# get_method_response()

def get_all_comments():
    url = "https://gorest.co.in/public/v2/users/7373670/posts"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text, response.status_code)


# get_all_comments()


def get_specific_number_users():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())
    pprint(response.status_code)


# get_specific_number_users()


def create_new_entry_using_post():
    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2025,
            "price": 2000.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "5 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)


#create_new_entry_using_post()

# new_object_id = ff808181932badb601953d95479c19c6


def update_field_available_object_using_put(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    # payload = json.dumps({
    #     "name": "Apple MacBook Pro 20",
    #     "data": {
    #         "year": 2025,
    #         "price": 2000.99,
    #         "CPU model": "Intel Core i10",
    #         "Hard disk size": "5 TB",
    #         "color": "silver"
    #     }
    # })

    # remove any field
    payload = json.dumps({
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2025,
            "price": 2000.99,
            "CPU model": "Intel Core i10",
        }
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)


# update_field_available_object_using_put("ff808181932badb601953d95479c19c6")
# ff808181932badb601953da1530319d0

update_field_available_object_using_put("ff808181932badb601953da1530319d0")

def update_field_value_of_object_using_patch(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 21",
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)


# update_field_value_of_object_using_patch("ff808181932badb601953d95479c19c6")


def delete_object_with_object_id(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.json())
    print(response.status_code)


#delete_object_with_object_id("ff808181932badb601953d95479c19c6")


# {'message': 'Object with id = ff808181932badb601953d95479c19c6 has been deleted.'}


def get_specific_id_details(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    pprint(response.json())
    pprint(response.status_code)

#get_specific_id_details("ff808181932badb601953d95479c19c6")
# {'error': 'Oject with id=ff808181932badb601953d95479c19c6 was not found.'}
