import sys
import time

from core.downloader import HTTPDownloader


def parse_arguments():
    url, chunk_length = sys.argv[1:]
    chunk_length = int(chunk_length)
    return url, chunk_length


if __name__ == "__main__":
    url, chunk_length = parse_arguments()
    downloader = HTTPDownloader(url, chunk_length)
    while True:
        downloader.download_chunk()
        content = downloader.last_chunk
        if content:
            print (len(content))
        else:
            print ("---")
            time.sleep(1)
