'''
The program will prompt for a URL, read the JSON data
from that URL using urllib and then parse and
extract the comment counts from the JSON data,
compute the sum of the numbers in the file
and enter the sum below:
- Actual data: http://py4e-data.dr-chuck.net/comments_706604.json
- Dependencies: pip3 install bs4
'''
import json
import urllib.request
import urllib.parse
import urllib.error

count = 0
sum = 0

url = input("Enter location: ")
print("Retrieving", url)
urlHandle = urllib.request.urlopen(url)
data = urlHandle.read()
print("Retrieved", len(data), "characters")

info = json.loads(data)

for i in info['comments']:
    count = count+1
    sum = sum + i['count']

print("Count:", count)
print("Sum:", sum)
