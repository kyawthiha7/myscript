from Crypto.Cipher import DES3 as _des
import base64
import sys
import argparse
import optparse

key = 'abcdefghijklmnop'
IV = 'ABCDEFGH'

class des:
	def __init__(self, key, IV, mode=_des.MODE_CBC):
		self.key = key
		self.IV = IV
		self.mode = mode
		self.size = 8

	def encrypt(self,string):
		length = 8 - len(string) % 8
		pad = chr(length) * length
		new = string + pad
		cipher = _des.new(self.key, self.mode, self.IV)
		data = cipher.encrypt(new)
		return base64.b64encode(data)

	def unpad(self, string):
		pad_size = ord(string[-1])
		print "padding size : " +str(pad_size)
		print "decrypted string : " +string[:-pad_size]

	def decrypt(self,string):
		encrypt = _des.new(key, _des.MODE_CBC, IV)
		decode_string = base64.b64decode(string)
		plaintext = encrypt.decrypt(decode_string)
		return self.unpad(plaintext)

if len(sys.argv) == 1:
	print "Usage : python 3des.py -d/e -c cipher -t test"
	sys.exit()

parser = optparse.OptionParser(description= "Triple DES Encrypt Decrypt Script ", prog="3des.py")

parser.add_option('-d','--decrypt',dest='decrypt',action="store_true",help='Triple DES Decrypt Method') 
parser.add_option('-e','--encrypt',dest='encrypt',action="store_true",help='Triple DES Encrypt Method')
parser.add_option('-c','--cipher',dest='cipher',help='Cipher Text')
parser.add_option('-t','--text',dest='text', type='string',help='String to encrpyt')

options, args = parser.parse_args()

if (options.encrypt):
	ctext = options.text
	new = des(key,IV)
	print new.encrypt(ctext)

if (options.decrypt):
	ctext = options.cipher
	new = des(key,IV)
	print new.decrypt(ctext)
