import sys
import time
import os

from core.downloader import HTTPDownloader

#from subprocess import Popen
import subprocess
#import subprocess32

def parse_arguments():
    url, chunk_length = sys.argv[1:]
    chunk_length = int(chunk_length)
    return url, chunk_length


if __name__ == "__main__":
    url, chunk_length = parse_arguments()
    print ("Init DW")
    downloader = HTTPDownloader(url, chunk_length)

    finalpath = "/tmp/thumbs/"
    pipe_read, pipe_write = os.pipe()
    ffmpeg_bin = "/opt/ffmpeg/bin/ffmpeg"
    cmd = [ffmpeg_bin, '-i', "pipe:0", '-f', 'image2',
               '-vf', 'fps=fps=1',  finalpath + '%05d.jpg']
    #cmd = ["cat"]
    print (" ".join(cmd))    
    ffmpeg_proc = subprocess.Popen(cmd, stdin=pipe_read)
    pipef = os.fdopen(pipe_write, 'wb')
    #file_test = open("/tmp/test.mp4", 'wb')

    while True:
        downloader.download_chunk()
        content = downloader.last_chunk
        if content:
            print (len(content))
            #Process chunk
            pipef.write(content)
            #file_test.write(content)
            print ("  Data sent to ffmpeg")
        else:
            print ("---")
            time.sleep(2)
