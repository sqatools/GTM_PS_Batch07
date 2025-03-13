common_url = "https://api.restful-api.dev/objects"

add_object_payload = {
   "name": "Apple MacBook Pro 160",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

ad_object_headers = {
        'Content-Type': 'application/json'
    }


users_url = "https://gorest.co.in/public/v2/users"
api_access_token = "2c23a02b621b71b08c567fab7d5a82459005026b8e4f14ac936f4d3e3b99e9e7"
users_headers = {'Authorization': f"Bearer {api_access_token}"}