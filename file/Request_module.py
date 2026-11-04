import requests
response = requests.get("https://www.google.com")
print(response.text)

print("\n")

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'foo',
     "body":  'bar',
     "userId": 1,
}
headers = {
    'content-type': 'application/json; charset=UTF-8',}
response = requests.post(url,headers=headers,json=data)

print(response.text)