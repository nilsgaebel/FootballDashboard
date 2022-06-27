import requests
import json
headers = {'X-Auth-Token': 'Token'}
r = requests.get("https://api.football-data.org/v4/competitions/CL/teams",headers=headers)

print('Status response of the request: ', r.status_code)

json = json.loads(r.text)
team_names = []
for t in json['teams']:
     team_names.append(t['name'])

print("team names in UCL: ", team_names)

r2 = requests.get("https://api.football-data.org/v4/matches",headers=headers)

print('Status response of the request: ', r2.status_code)
test = r2.text
json_2 = json.loads(test)
