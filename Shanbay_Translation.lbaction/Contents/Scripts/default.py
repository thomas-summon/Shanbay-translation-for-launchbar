#!/usr/bin/env python3
#
# LaunchBar Action Script
#
import sys
import requests
import json

item=[]

ARGV = str(sys.argv[1])

Response = requests.get('https://api.shanbay.com/bdc/search/?word=' + ARGV)

data_0 = json.loads(Response.text)

judge = int(data_0['status_code'])

if judge == 1 :
    print ('Not found!')
    
else : 
    data_1 = data_0['data']
    data_2 = data_1['definition']
    item.append(data_2)
    print (item[0])
