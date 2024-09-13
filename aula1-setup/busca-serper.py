import http.client
import json

API_KEY = 'SUACHAVEAPIAQUI'

conn = http.client.HTTPSConnection("google.serper.dev")
payload = json.dumps({
    "q": "Como fazer um hambúrguer caseiro?",
    "gl": "br",
    "hl": "pt-br",
})
headers = {
    'X-API-KEY': API_KEY,
    'Content-Type': 'application/json'
}
conn.request("POST", "/search", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
