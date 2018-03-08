import requests
import os
import sys
import argparse


''' 
	S3 bucket finder

''' 

if len(sys.argv) == 1:
	print "Usage : python s3.py paramter \n python s3.py -h "
	sys.exit()

parser = argparse.ArgumentParser(description=" - S3 bucker finder \n",
				prog="s3")

parser.add_argument('-r','--region',dest='region',help='AWS region default is us-west-1')
parser.add_argument('-d','--domain',dest='domain',help='AWS domain or file list') 

parser.set_defaults(region="us-west-1")

def checkBucket(bucket, region):

	bucketDomain = "http://"+bucket+".s3-" + region + ".amazonaws.com"
	r = ()
	try:
		r = requests.head(bucketDomain)
	except requests.exceptions.ConnectionError:
		print "no bucket found"

	if r.status_code == 200:	
		return "Bucket Found: " +bucketDomain
	
	if r.status_code == 301:
		return "redirect region try with region parameter",r.headers["x-amz-bucket-region"]
		
	if r.status_code == 404:
		return "No bucket"

	if r.status_code == 403:
		return "forbidden"

	else:
		return "no information"


args = parser.parse_args()
region = args.region

result = checkBucket(args.domain,region)

print result
