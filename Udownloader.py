#!/usr/bin/python
import re
import subprocess

s = \
  """ paste your youtubelink here
      paste your youtubelink here
      paste your youtubelink here"""


lines = re.split('\n',s)
for oup in lines:
    cmd = 'youtube-dl '+oup
    print 'downloading  '+oup
    subprocess.call(cmd, shell=True)
#this will download the youtube videos in the script directoty
        
