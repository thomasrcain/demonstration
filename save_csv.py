import requests
import csv

# Simple interactive script querying an API

url = "http://www.omdbapi.com/"

title = input("Enter a movie that you like: ")
# year = input("What year was it released? ")

# Populate the query string with your apikey and title
querystring = {"apikey":"9b96d509", "t":title}

# Use the request method
# Returns a requests.models.Request obj
response = requests.request("GET", url, params=querystring)
print(type(response))

# Use the json method in requests module to convert the json to a dict
thejson = response.json()
print(type(thejson))

# Iterate over key/value pairs in dict and print them
for key, value in thejson.items():
    print(key, ' : ', value)

'''
# time to create a CSV
csv_fn = title+".csv"
with open(csv_fn, 'w', newline='') as csvfile:
    fieldnames = thejson.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(thejson)
'''
