import json
import ssl
import urllib.request
import urllib.parse
import urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Stroring the given parameters
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
data_address = input("Enter location: ")

params = {"address": data_address, "key": api_key}
paramsurl = urllib.parse.urlencode(params)

url = serviceurl.strip() + paramsurl.strip()
print("Retrieving:", url)

# Obtaining and reading the data
try:
    data_read = urllib.request.urlopen(url, context=ctx).read()
    data = data_read.decode()
    print("Retrived", len(data), "characters")

    # Parsing the data and looking for location info
    jsondata = json.loads(data)

    if 'status' not in jsondata or jsondata['status'] != 'OK':
        print("Error: Failure to retrieve")
        print(data)

    # Set and print out location info to the console
    place_id = jsondata["results"][0]["place_id"]
    print("Place id", place_id)
except:
    print("Error. Please try again.")
    print("-"*30)
    print(data)
