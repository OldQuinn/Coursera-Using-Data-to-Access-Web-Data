import urllib.request, urllib.parse, urllib.error
import json

url=input("Enter location: ")
#url = ' http://py4e-data.dr-chuck.net/comments_10141.json'

#open url
url_open = urllib.request.urlopen(url)

#extract data
data = url_open.read()

#put the data into a dictionary
data_parsed = json.loads(data)

'''print the sum of all 'count' occurrences. The file has the following structure:
 {
  "note":"This file contains the actual data for your assignment",
  "comments":[
    {
      "name":"abc",
      "count":100
    },
    {
      "name":"cde",
      "count":77
    }, ...
  }
'''
total = 0
for item in data_parsed['comments']:
    total += int(item['count'])

print ('Total: ', total)