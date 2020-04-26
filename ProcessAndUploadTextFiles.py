import os
import requests
import json

files = os.listdir("/data")

print("Your files :")
print(files)

data = []
for file in files:
  for line in file:
    line.strip('\n')
  with open("/data/"+file, 'r') as f:
    dict = {
    "title":f.readline().strip("\n"),
    "name":f.readline().strip("\n"),
    "date":f.readline().strip("\n"),
    "feedback":f.readline().strip("\n"),
    }
    data.append(dict)
    print(file + " terminated  *****")

url = '{url}'
newHeaders = {'Content-type': 'application/json'}
for item in data:
   item_json = json.dumps(item)
   print('loading item '+ str(data.index(item)+1) )
   x = requests.post(url, data = item_json,headers=newHeaders)
   response = requests.get('{url}')
   print("get method status: " + str(response.status_code))
   print("post method status: " + str(x.status_code))

