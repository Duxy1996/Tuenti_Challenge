#!/usr/bin/python           
import httplib, urllib
params = urllib.urlencode({})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("52.49.91.111:8443")
conn.request("POST", "/cgi-bin/query", params, headers)
response = conn.getresponse()
print response.status 
print response.reason
data = response.read()
print data
conn.close()
outfile = open('texto.txt', 'w')
outfile.write(data)
outfile.close()