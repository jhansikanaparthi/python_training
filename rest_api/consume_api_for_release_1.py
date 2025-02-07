"""
requests: To access API
"""
print("Accessing weather API")
print("-"*20)
# -------------

import requests

api_response = requests.get("https://demoqa.com/utilities/weather/city/bangalore")
api_data = api_response.json()

print("api_data:", api_data, end="\n\n")
print("type of api_data:", type(api_data), end="\n\n")

print("#"*40, end="\n\n")
############################

print("GET: Getting all records")
print("-"*20)
# -------------

try:
    import requests
    api_response = requests.get("http://127.0.0.1:5000/getdbdata")
    api_data = api_response.json()
    print("api_data:", api_data, end="\n\n")
    print("type of api_data:", type(api_data), end="\n\n")
except Exception as e:
    print("Error Details:", e, end="\n\n")
    print("""
    Not able to access API,
    Please make sure to run my_rest_api_release_1.py
    """)
    exit()

print("#"*40, end="\n\n")
############################