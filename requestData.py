import requests
import json
headers = {'X-Auth-Token': 'TOKEN'} # token has to be replaced
r = requests.get("https://api.football-data.org/v4/competitions/CL/matches",headers=headers)

print('Status response of the request: ', r.status_code)

json = json.loads(r.text)
for t in json['matches']:
    print(t['homeTeam'])  
    
print("DONE")

