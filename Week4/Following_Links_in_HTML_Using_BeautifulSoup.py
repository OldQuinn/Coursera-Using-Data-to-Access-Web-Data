#Following_Links_in_HTML_Using_BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url="http://py4e-data.dr-chuck.net/known_by_Reagan.html"
#count=7
#position=18
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

names = []

while count > 0:
    print ("retrieving: {0}".format(url))
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1

print (names[-1])