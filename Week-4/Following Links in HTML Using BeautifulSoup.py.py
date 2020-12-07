import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL:  ')
toCOunt = int(input('Enter Count: '))
call = int(input('Enter Number of Times: '))

for i in range (call):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    counter = 1
    tagval = {}
    for tag in tags:
        tagval[counter] = tag.get('href', None)
        counter = counter + 1
    
    positionLink = tagval[toCOunt]
    print(positionLink)
    url = positionLink
