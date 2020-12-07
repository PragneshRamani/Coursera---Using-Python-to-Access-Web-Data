from bs4 import BeautifulSoup
import re
import urllib.request

def getval(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('span')

    numbers = []
    for tag in tags:
        number = (tag.contents)
        numbers.append(number)

    sum=0
    for number in numbers:
        for num in number:
            sum= sum + int(num)

    print(sum)

getval('http://py4e-data.dr-chuck.net/comments_751365.html')