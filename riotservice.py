import secrets
import requests
import json

baseurl = secrets.riotapiurl['na']
headers = {'X-Riot-Token': secrets.riotkey}

def get_summoner(summonerName: str):
    apiurl = baseurl + f'/lol/summoner/v3/summoners/by-name/{summonerName}'

    response = requests.get(apiurl, headers=headers)

    jsonstuff = json.loads(response.content)

    return jsonstuff

