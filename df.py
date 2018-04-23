#!/usr/bin/python 

import sys
import requests
import os
import argparse
import optparse

def listvendor_callback(option, opt_str, value, parser):
	print "support vendor:\n\x1b[6;30;42m akama \n aliyun \n azure \n beluga \n cdn77 \n chinacache \n cloudfront \n fastly \n maxcdn \n netlify \n stackpath \x1b[0m"
	

print('''### domain fronting finder 
### domain lists can be found @ https://github.com/vysec/DomainFrontingListsa
### script idea derive from https://github.com/yeyintminthuhtut/Lazy-RedTeamer-Scripts\n''')

if len(sys.argv) == 1:
	print "Usage : python df.py paramter \n python df.py -h \n python fd.py -H host -v cloudfront"
	sys.exit()

parser = optparse.OptionParser(description="  Domain Finding Script \n",
				prog="df.py")

parser.add_option('-H','--domain',dest='host',help='your host for fronting') 
parser.add_option('-v','--vendor',dest='vendor',help='CDN Vendor')
parser.add_option('-l','--listvendor',dest='vendorlist',help='vendor list', action='callback', callback=listvendor_callback)

options, args = parser.parse_args()

if options.vendor == 0:
	print "Vendor parameter is requier"
   
if (options.vendor == "cloudfront") or (options.vendor == "akamai") or (options.vendor == "azure") or (options.vendor == "cdn77"):
	with open("domainlists/"+args.vendor+".txt", 'r') as f:
                for line in f:
                        host = line.strip()
                        hosts = "http://"+host+"/t33t.txt"
                        headers = {'Host': args.host}
                        try:
                                r = requests.get(hosts, headers=headers)
                        except requests.exceptions.ConnectionError:
                                print host+ "\x1b[0;30;41m"+" Connection Error"+"\x1b[0m"
                        if r.status_code == 200:
                                print "[~] " +host+ ": \x1b[6;30;42m"+ " Frontable" +"\x1b[0m"
                        else :
                                print "[~] " +host+ ": \x1b[3;30;47m"+ "not Frontable" +"\x1b[0m "

#else:
#	print "support vendor:\n\x1b[6;30;42m akama \n aliyun \n azure \n beluga \n cdn77 \n chinacache \n cloudfront \n fastly \n maxcdn \n netlify \n stackpath \x1b[0m"
	
