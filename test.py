import urllib2
import sys


def download_chunk(url, start, end):
    req = urllib2.Request(url)
    req.headers['Range'] = 'bytes=%s-%s' % (start, end - 1)
    f = urllib2.urlopen(req)
    return f.read()

if __name__ == "__main__":
    url, chunk_length = sys.argv[1:]
    chunk_length = int(chunk_length)
    i = 0
    while (True):
        content = download_chunk(url, i*chunk_length, (i+1)*chunk_length)
        if not content:
            break
        print (len(content))
        i += 1
