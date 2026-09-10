import urllib.request
import json

web_url = urllib.request.urlopen("http://www.allegion.com")

print("Result code:", web_url.getcode())

data = web_url.read()
#print(data) #html format web page

#data = data.decode('utf-8')
#print(data)

theJSON = json.loads(data)

print(theJSON["test"])