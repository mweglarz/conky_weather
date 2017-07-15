import yaml

class Config:

    def __init__(self, path = None):
        self.configPath = path if path is not None else "weather_config.yml"
        with open(self.configPath, 'r') as ymlFile:
            config = yaml.load(ymlFile)
            weather = config['weather']
            self.url = weather['url']
            self.clientId = weather['clientId']
            self.clientSecret = weather['clientSecret']
            self.oauthUrl = weather['oauthUrl']

        if self.url is None or self.clientId is None or \
            self.clientSecret is None or self.oauthUrl is None:

            raise Exception("wrong config for weather")
