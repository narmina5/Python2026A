########################################## JSON ###############################################

"JSON"
"""
JSON	    Python
=====       ============
object	    dict
array	    list/tuple
string	    str
number	    int/float
true/false	True/False
null	    None
"""

import json

my_var = {
    "abc": True,
    "def": None,
    "ghi": [1,2,3]
}
with open("my_var.json", "w") as file:
    json.dump(my_var, file)

my_str = json.dumps(my_var)
print(str(my_var))
print(my_str)

with open("dummy.json", "r") as file:
    result = json.load(file)
    print(type(result))
    print("Result:", result)

my_result = json.loads(my_str)
print(type(my_result))


my_var = {
    "title": "CursorAI",
    "max_limit": 2500,
    "question": "ChatGPT ve Cursor birlikde nece ishleyir"
}


"""
json.dump(obj, file)    - python dict --> JSON Fayl
json.dumps(obj)         - python dict --> JSON String
json.load(file)         - JSON Fayl --> Python Dict
json.loads(string)      - JSON Fayl --> JSON String
"""


########################################## RANDOM ###############################################

"""
import random
print(random.random()) # 0.0 – 1.0 arasında təsadüfi float
print(random.randint(1,10)) # 1 – 10 arasında təsadüfi integer (daxil)
print(random.uniform(5,15)) # 5 – 15 arasında təsadüfi float
"""

import random
print(random.random()) # 0.0 – 1.0 arasında təsadüfi float
print(random.randint(1,100)) # 1 – 100 arasında təsadüfi integer (daxil)
print(random.uniform(5,15)) # 5 – 15 arasında təsadüfi float




"""
import random

a = random.random()
b = random.randint(-50, 50)
c = random.randrange(5, 100, 5)
print(a)
print(b)
print(c)
"""


"""
import random
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits)) # 1 təsadüfi element
print(random.sample(fruits, 2)) # 2 fərqli element (unique)
print(random.choices(fruits, k=3)) # 3 element (təkrar ola bilər)
random.shuffle(fruits) # list-i qarışdırır (yerində)
print(fruits)
"""
"""
import random
fruits = ["apple", "banana", "cherry", "date"]

print(random.choice(fruits)) # 1 təsadüfi element
print(random.sample(fruits, 2)) # 2 fərqli element (unique)
print(random.choices(fruits, k=15)) # 3 element (təkrar ola bilər)

random.shuffle(fruits) # list-i qarışdırır (yerində)

print(fruits)
"""


"""
fruits = ["apple", "banana", "cherry", "date"]
print(secrets.choice(fruits)) # təhlükəsiz seçim (random.choice əvəzinə)
"""

"Tokenlər"
"""
import secrets
print(secrets.token_bytes(16)) # təsadüfi byte string (16 byte)
print(secrets.token_hex(16)) # hex string (32 simvol)
print(secrets.token_urlsafe(16)) # URL-də təhlükəsiz istifadə oluna bilən token
"""
import secrets

print(secrets.token_hex())
print(secrets.token_urlsafe(16))

########################################## REQUESTS ##########################################
import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.text)
print(response.status_code)


"""
import requests

# Sending a GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)  # 200 if request is successful
print(response.text)          # Returns the response content as a string

# Sending a POST request
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)  # 201 if created
print(response.json())       # Returns the response content as JSON
"""
"""
# Sending a GET request with parameters
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.status_code)
print(response.json())  # Parsed JSON data from the response
"""

"""
# Sending a request with headers
headers = {"Authorization": "Bearer your_token"}
response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
print(response.status_code)
"""

"""
# Sending a PUT request to update data
data = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)
print(response.status_code)  # 200 if updated successfully
print(response.json())
"""

"""
# Sending a DELETE request to delete data
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 if successfully deleted
"""