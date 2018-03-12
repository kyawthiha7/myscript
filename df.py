#!/usr/bin/python

import sys
import requests
import os
import argparse


print('''### domain fronting finder
### domain lists can be found @ https://github.com/vysec/DomainFrontingListsa
### script idea derive from https://github.com/yeyintminthuhtut/Lazy-RedTeamer-Scripts\n''')

if len(sys.argv) == 1:
        print "Usage : python df.py paramter \n python df.py -h"
        sys.exit()

parser = argparse.ArgumentParser(description="  Domain Finding Script \n",
                                prog="s3")


parser.add_argument('-f','--file',dest='file',help='file of domain')
parser.add_argument('-H','--domain',dest='host',help='your host for fronting')
parser.add_argument('-v','--vendor',dest='vendor',help='domain vendor:cloudfront,akamai,cloudflare,etc..')

args = parser.parse_args()

if args.vendor == 0:
        print "Vendor parameter is require"


if (args.vendor == "aws") or (args.vendor == "akamai") or (args.vendor == "azure") or (args.vendor == "cdn77"):
        with open(args.file, 'r') as f:
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

else :
        print "[~] vendor name error \n[~] support vendor akamai, aliyun, azure,beluga, cdn77, chinacache, cloudfront, fastly, maxcdn, netlify, stackpath"
