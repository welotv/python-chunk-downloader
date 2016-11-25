import urllib2


class HTTPDownloader:

    def __init__(self, url, size):
        self.url = url
        self.last_byte = 0
        self.size = size

    @property
    def new_last_byte(self):
        return self.last_byte + self.size

    @property
    def range_(self):
        return (self.last_byte, self.new_last_byte - 1)

    def get_chunk(self):
        req = urllib2.Request(self.url)
        req.headers['Range'] = 'bytes=%s-%s' % self.range_
        f = urllib2.urlopen(req)
        self.last_byte = self.new_last_byte

        return f.read()
