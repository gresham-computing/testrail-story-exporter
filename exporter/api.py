import requests


class TestRailApi:
    def __init__(self, config):
        self.server = config['server']
        self.username = config['username']
        self.api_key = config['apikey']

    def _url(self):
        return 'https://%s/index.php?' % self.server

    def _request(self, endpoint):
        uri = self._url() + endpoint
        r = requests.get(uri,
                         auth=(self.username, self.api_key),
                         headers={'Content-Type': 'application/json'})
        return r.json()

    def get_sections(self, suite_id):
        return self._request('/api/v2/get_sections/%s' % suite_id)
