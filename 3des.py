from Crypto.Cipher import DES3 as _des
import base64
import sys
import argparse
import optparse

key = 'abcdefghijklmnop'
IV = 'ABCDEFGH'

def unpad(self, string):
	pad_size = ord(string[-1])
	print "padding size : " +str(pad_size)
	print "decrypted string : " +string[:-pad_size]
def encrypt(string):
	pad_len = 8 -len(string) %8
	pad = string+chr(pad_len) * pad_len
	print pad
        cipher = DES3.new(key, DES3.MODE_CBC, IV)
        ctext = cipher.encrypt(pad)
        return base64.b64encode(ctext)	

def decrypt(string):
	encrypt = DES3.new(key, DES3.MODE_CBC, IV)
	decode_string = base64.b64decode(string)
	plaintext = encrypt.decrypt(decode_string)
	return unpad(plaintext)


if len(sys.argv) == 1:
	print "Usage : python 3des.py -d/e -c cipher -t text"
	sys.exit()

parser = optparse.OptionParser(description= "Triple DES Encrypt Decrypt Script ", prog="3des.py")

parser.add_option('-d','--decrypt',dest='decrypt',action="store_true",help='Triple DES Decrypt Method') 
parser.add_option('-e','--encrypt',dest='encrypt',action="store_true",help='Triple DES Encrypt Method')
parser.add_option('-c','--cipher',dest='cipher',help='Cipher Text')
parser.add_option('-t','--text',dest='text', type='string',help='String to encrpyt')

options, args = parser.parse_args()

if (options.encrypt):
	ctext = options.text
	print encrypt(ctext)

if (options.decrypt):
	ctext = options.cipher
	print decrypt(ctext)
