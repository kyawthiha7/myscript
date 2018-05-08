from Crypto.Cipher import DES3
import base64
import sys
import optparse

key = 'abcdefghijklmnop'
IV = 'ABCDEFGH'

def encrypt(string):
	length = 8 - len(string) % 8
	pad = chr(length) * length
	new = string + pad
	cipher = DES3.new(key, DES3.MODE_CBC, IV)
	data = cipher.encrypt(new)
	return base64.b64encode(data)

def unpad(string):
	pad_size = ord(string[-1])
	print "padding size : " +str(pad_size)
	print "decrypted string : " +string[:-pad_size]

def decrypt(string):
	if len(string) % 8:
		raise ValueError("Input data is not padded")
	encrypt = DES3.new(key, DES3.MODE_CBC, IV)
	decode_string = base64.b64decode(string)
	plaintext = encrypt.decrypt(decode_string)
	return unpad(plaintext)

if len(sys.argv) == 1:
	print "Usage : python 3des.py -d/e -c cipher -t test"
	sys.exit()

parser = optparse.OptionParser(description= "Triple DES Encrypt Decrypt Script ", prog="3des.py")

parser.add_option('-d','--decrypt',dest='decrypt',action="store_true",help='Triple DES Decrypt Method') 
parser.add_option('-e','--encrypt',dest='encrpyt',action="store_true",help='Triple DES Encrypt Method')
parser.add_option('-c','--cipher',dest='cipher',help='Cipher Text')
parser.add_option('-t','--text',dest='text', type='string',help='String to encrypt')

options, args = parser.parse_args()

if (options.encrpyt):
	ctext = options.text
	print encrypt(str(ctext))

if (options.decrypt):
	ctext = options.cipher
	decrypt(ctext)
