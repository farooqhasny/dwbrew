#!/usr/bin/python

import os
import cgitb
cgitb.enable()
import json

try:
        #get the list of log files
        path = '/home/linaro/Projects/brew/logs'
        mtime = lambda f: os.stat(os.path.join(path, f)).st_ctime
        dl = list(sorted(os.listdir(path), key=mtime))

        data = []
        for file in dl:
                f = open(path+"/"+file,'r')
                for line in f:
                        fields = line.strip('\n').split(',')
                        data.append({"date":file,"time":fields[0],"temp":fields[1],"sg":fields[2]})

        print("Content-Type: text/html")
        print("")
        print(json.dumps(data))

except:
        print("Content-Type: text/html")
        print("")
        print("Exception getting data")
