import secrets
import requests
import json

baseurl = secrets.riotapiurl['na']
headers = {'X-Riot-Token': secrets.riotkey}

def get_summoner(summonerName: str):
    apiurl = baseurl + f'/lol/summoner/v3/summoners/by-name/{summonerName}'

    response = requests.get(apiurl, headers=headers)

    jsonstuff = json.loads(response.content)
    print(jsonstuff)
    return jsonstuff


def is_in_match(summonerId: int):
    apiurl = baseurl + f'/lol/spectator/v3/active-games/by-summoner/{summonerId}'

    response = requests.get(apiurl, headers=headers)

    print(response)

    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None


def get_champion(championId: int):
    apiurl = baseurl + f'/lol/static-data/v3/champions/{championId}'

    response = requests.get(apiurl, headers=headers)

    return json.loads(response.content)
