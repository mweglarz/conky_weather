from MWWeatherConfig import Config
from RequestService import RequestService

class MWWeather:

    def __init__(self, config):
        self.config = config
        self.requestService = RequestService(url = config.url,
                                             clientId = config.clientId,
                                             clientSecret = config.clientSecret,
                                             oauthUrl = config.oauthUrl)

    def run(self):
        weatherJSON = self.requestService.makeRequest()
        print("weatherJSON = %s" % weatherJSON)
