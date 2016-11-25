import urllib2
import sys


class HTTPDownloader:

    def __init__(self, url):
        self.url = url
        self.last_byte = 0

    def get_chunk(self, size):
        req = urllib2.Request(url)

        new_last_byte = self.last_byte + size
        req.headers['Range'] = 'bytes=%s-%s' % (
            self.last_byte, new_last_byte - 1)
        self.last_byte = new_last_byte

        f = urllib2.urlopen(req)
        return f.read()


def parse_arguments(args):
    url, chunk_length = args
    chunk_length = int(chunk_length)
    return url, chunk_length


if __name__ == "__main__":
    url, chunk_length = parse_arguments(sys.argv[1:])
    downloader = HTTPDownloader(url)
    while True:
        content = downloader.get_chunk(chunk_length)
        if not content:
            break
        print (len(content))
