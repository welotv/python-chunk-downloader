from urllib import request
from http import client


class HTTPDownloader:

    def __init__(self, url, size):
        self.url = url
        self.last_byte = 0
        self.size = size
        self.last_chunk = None

    @property
    def _range(self):
        return (self.last_byte, self.last_byte + self.size - 1)

    def build_request(self):
        req = request.Request(self.url)
        req.headers['Range'] = 'bytes=%s-%s' % self._range
        return req

    def get_response(self):
        req = self.build_request()
        response = request.urlopen(req)
        try:
            chunk = response.read()
        except client.IncompleteRead as e:
            chunk = e.partial
        return chunk

    def download_chunk(self):
        chunk = self.get_response()
        self.last_chunk = chunk
        self.last_byte += len(self.last_chunk)
