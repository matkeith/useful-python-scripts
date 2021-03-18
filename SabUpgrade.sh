#!/bin/bash
$("/home/MyUser/SabUpgradeChecker.py")
RESULT=$?

#echo $RESULT
if [ $RESULT -eq 0 ]
then
cd /home/MyUser/docker/newsgroupdl
/usr/bin/docker-compose pull && /usr/bin/docker-compose up -d

fi
