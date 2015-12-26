URL = {
    'base': 'https://{proxy}.api.pvp.net/{url}',
    'summoner_by_name': 'api/lol/{region}/v{version}/summoner/by-name/{names}',
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',
    'get_champion': 'api/lol/static-data/{region}/v1.2/champion/{id}',
    'data_dragon': 'http://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{champion}'
}

API_VERSIONS = {
    'summoner': '1.4',
    'data_dragon': '5.24.2'
}

REGIONS = {
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'euwest': 'EUW1'
}
