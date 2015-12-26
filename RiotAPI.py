import requests
import RiotConsts as Consts


class RiotAPI(object):

    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, give_region, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                    proxy=give_region,
                    url=api_url),
            params=args
        )
        print(response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            region=self.region,
            version=Consts.API_VERSIONS['summoner'],
            names=name,
        )
        return self._request(api_url, self.region)

    def get_current_game(self, summoner_id):
        api_url = Consts.URL['current_game'].format(
            platformId=Consts.REGIONS['euwest'],
            summonerId=summoner_id
        )
        return self._request(api_url, self.region)

    def get_champion_data(self, championId):
        api_url = Consts.URL['get_champion'].format(
            region='euw',
            id=championId
        )
        return self._request(api_url, 'global', params={'champData': 'image'})

    def get_league_data(self, summoner_id):
        api_url = Consts.URL['league_data'].format(
            region=self.region,
            summonerId=summoner_id
        )
        return self._request(api_url, self.region)