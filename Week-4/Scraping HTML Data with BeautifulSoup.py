'''
In this assignment you will write a Python program to use urllib
to read the HTML from the data files below,
and parse the data, extracting numbers
then compute the sum of the numbers in the file

if you haven't install BeautifulSoup4 before
please run: pip3 install bs4
'''
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup("span")

count = 0
sum = 0

for tag in tags:
    temp = int(tag.text)
    count += 1
    sum += temp

print("Count", count)
print("Sum", sum)
