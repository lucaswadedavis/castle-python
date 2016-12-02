import json
import requests

class Castle(object):

    def __init__(self, api_secret=None, request_metadata=None, api_url='https://api.castle.io/v1/'):
        self.request_metadata = request_metadata
        self.api_secret = api_secret
        self.api_url = api_url
        self.timeout = 3000

    def track(self, name='', user_id='', details={}):
        url = '%s/events' % (self.api_url)
        data = {'name': name, 'user_id': str(user_id), 'details': details}
        requests.post(url=url, data=data, headers=self.request_metadata, auth=('', self.api_secret), timeout=self.timeout)
