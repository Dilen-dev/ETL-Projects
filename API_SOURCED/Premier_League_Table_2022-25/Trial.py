import requests

url = "https://v3.football.api-sports.io/standings"

payload={}
headers = {
  'x-apisports-key': '0b15dcd2620348c1085dab3a378688d7',
}

response = requests.request("GET", url, headers=headers,params={"league": 39, "season": 2023},data=payload)

print(response.text)