import requests
import json
import time

print("Please provide an API key from urlscan.io (https://urlscan.io/user/signup):")
APIkey = input()
if APIkey == '':
    APIkey = secrets.py
    pass
else:
    pass

print("Enter the target website below:")
target = input()
# print(target)

headers = {'API-Key': APIkey, 'Content-Type': 'application/json'}
data = {"url": target, "visibility": 'private'}

try:
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print("Error encountered: " + e)
    raise SystemExit(e)

data = json.loads(response.text)
api = data['api']
print("****** " + api + " *****")

time.sleep(3)

try:
    response = requests.post(api, headers=headers)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
    raise SystemExit(e)

data = response.json()

# data = json.loads(response.text)

print(data)
print(data['screenshotURL'])
print(data['asn'])

# print(headers)
# print(data)
# print(response)
# print(response.json())

uuid = (data["uuid"])

example = (data["screenshotURL"])

print("Screenshot URL:")
print(example)
url = 'https://urlscan.io/screenshots/' + uuid + '.png'
print(url)

response = requests.post(url, headers=headers,
                         data=json.dumps(data))

data = json.loads(response.text)
ASN = (data['asn'])
print(ASN)

# ASN = "https://urlscan.io/api/v1/result/" + uuid + "/meta/ASN/"

AbuseContact = "https://stat.ripe.net/data/abuse-contact-finder/data.json?resource=" + "ASN"

print(ASN)
print(AbuseContact)
