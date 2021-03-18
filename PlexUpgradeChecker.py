#!/usr/bin/env python3
import sys
import requests
from lxml import etree
success = False
token = 'blah'
uri = 'http://192.168.1.120:32400/status/sessions?X-Plex-Token=' + token

#print(uri)
#try:
response = requests.get(uri)
#print(response.content.strip())

root_node = etree.fromstring(response.content.strip())
viewer_count = int(root_node.get('size'))
#print(viewer_count)
if viewer_count == 0:
  success = True

if success:
  sys.exit(0)
else:
  sys.exit(1)
