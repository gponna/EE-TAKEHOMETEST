#!/usr/bin/python

from __future__ import print_function

# Script : queryusergists.py, is a script to query a GitHub user's gists
#
# Usage:  queryusergists.py [-h] <username>, where <username> is the Github user's username.
#
# Description : On query a user's gists, queryGists will register the current gists for that user and show the date of the latest gist. 
# The user will be registered in a file named "/tmp/queryusergists.<username>".
# Subsequent executions for the same username will tell you if a new gist has been added by the user.

import sys
import os
import argparse
try:
    import simplejson as json
except ImportError:
    import json
import datetime as dt
import urllib
import requests

# Parsing command line arguments

parser = argparse.ArgumentParser()
parser.add_argument("gitUser", help="Github username for gists query")
args = parser.parse_args()
GISTS_URL = 'http://api.github.com/users/' + args.gitUser + '/gists'

# Connecting to Github site and query user's gists and if not success, handle to exit

req = requests.get(GISTS_URL)
if req.status_code != 200:
    if req.status_code == 404:
        print ('Error: Github user "' + args.gitUser + '" not found.')
    else:
        req.raise_for_status()
    exit(255)
gist = json.loads(req.content)
if not gist:
    print ('Github user "' + args.gitUser + '" has not published any gists.')
    exit(1)

# Checking for any previous record of a query and if not, creating as a new entry
# If exists then to read the record file to get the previous check and compare to notify new gist.

configPath = '/tmp/queryusergists.' + args.gitUser
if not os.path.isfile(configPath):
    print('Github user "' + args.gitUser + '" gists have not been previously queried.')
    print('Creating checkpoint file: ' + configPath)
    try:
        configFile = open(configPath, "w")
        configFile.write(gist[0]['created_at'])
        configFile.close()
    except Exception as e:
        raise
else:
    try:
        configFile = open(configPath,"rw")
        stringDate = configFile.read()
    except Exception as e:
        raise
    lastCreateDate = dt.strptime(stringDate,'%Y-%m-%dT%H:%M:%SZ')
    currentLastCreateDate = dt.strptime(gist[0]['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    if currentLastCreateDate > lastCreateDate:
        print('Github user "' + args.gitUser + '" created a new gist since the previous query.')
        try:
            configFile.seek(0,0)
            configFile.write(gist[0]['created_at'])
        except Exception as e:
            raise
    else:
        print('Github user "' + args.gitUser + '" has not created a new gist since the previous query.')
    configFile.close()
exit(0)
