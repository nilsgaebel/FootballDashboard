import requests
import json
headers = {'X-Auth-Token': 'TOKEN'}

r1 = requests.get("https://api.football-data.org/v4/competitions/CL/teams",headers=headers)
print('Status response of the request: ', r1.status_code)

df_1 = json.loads(r1.text)
team_names = []
for t in df_1['teams']:
     team_names.append(t['name'])
print("team names in UCL: ", team_names)

r2 = requests.get("https://api.football-data.org/v4/matches/327117",headers=headers)
print('Status response of the request: ', r2.status_code)

df_2 = json.loads(r2.text)
homeTeam = df_2['homeTeam']
awayTeam = df_2['awayTeam']
print(homeTeam['name'], 'against', awayTeam['name'])
