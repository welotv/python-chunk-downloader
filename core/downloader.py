import urllib2


class HTTPDownloader:

    def __init__(self, url, size):
        self.url = url
        self.last_byte = 0
        self.size = size

    def get_chunk(self):
        req = urllib2.Request(self.url)

        new_last_byte = self.last_byte + self.size
        req.headers['Range'] = 'bytes=%s-%s' % (
            self.last_byte, new_last_byte - 1)
        self.last_byte = new_last_byte

        f = urllib2.urlopen(req)
        return f.read()
