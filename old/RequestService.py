from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.parse
import json
import base64

class RequestService:

    def __init__(self, url,
            clientId = None,
            clientSecret = None,
            oauthUrl = None):

        self.url = url
        self.clientId = clientId
        self.clientSecret = clientSecret
        base64string = base64.b64encode(bytes('%s:%s' % (clientId, clientSecret), 'utf8'))
        base64string = base64string.decode('utf8')
        print("base64 = %s" % base64string)
        self.base64 = base64string
        self.oauthUrl = oauthUrl
        self.headers = {}
        # print(("initialize RequestService with url %s" +
            #  " client = %s and secret = %s")
            #  % (url, clientId, clientSecret))

    def __request(self, url, parameters, headers, callback):
        data = urllib.parse.urlencode(parameters)
        data = data.encode('utf8')
        print('''
        making request with:
            url = %s,
            parameters = %s,
            headers = %s
        ''' % (url, parameters, headers))

        req = Request(url, data, headers)
        try:
            response = urlopen(req)

        except URLError as e:
            callback(None, e)

        else:
            callback(response, None)

### Weather request
    def makeRequest(self):
        data = {}
        headers = self.headers

        self.__request(self.url, data, headers, self.__weatherResponseHandler)

        req = Request(self.url, data, headers)

    def __weatherResponseHandler(self, response, error):
        if response is not None:
            self.__handleRequest(response)

        elif error is not None:
            self.__handleError(error)

        else:
            raise Exception('Unknown error in weatherResponseHandler')

    def __handleError(self, error):
        print("url error = %s" % error)
        if error.code == 401:
            self.authorizeRequest()

    def __handleRequest(self, response):
        print("url completed without error, response = %s" % response)

### Authorization request
    def authorizeRequest(self):
        url = self.oauthUrl
        parameters = {}
        parameters['client_id'] = self.clientId
        parameters['response_type'] = 'code'
        parameters['redirect_uri'] = 'oob'
        headers = {}
        self.__request(url, parameters, headers, self.__authorizeRequestHandler)

    def __authorizeRequestHandler(self, response, error):
        if response is not None:
            self.__handleAuthorizeResponse(response)
        else:
            print('unable to authorize request error = %s' % error)

    def __handleAuthorizeResponse(self, response):
        # responseString = response.read().decode('utf8')
        responseString = "OK"
        print('authorized response = %s' % responseString)
