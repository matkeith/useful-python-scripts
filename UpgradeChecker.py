#!/usr/bin/env python3
import sys
from requests import Session
from myconfig import *
success = False

uri = 'https://' + username + ':' + password + '@' + hostname + '/sabnzbd/api?apikey=' + apikey + '&output=json&mode=queue'

with Session() as s:
  try:
    response = s.get(uri)
    data = response.json()
#    print(data)
    if data.get("queue", {}).get("status") in ("Idle"):
      success = True
    else:
      success = False
  except:
    print("except")
    success = False

if success:
  print("success")
  sys.exit(0)
else:
  print("fail")
  sys.exit(1)
