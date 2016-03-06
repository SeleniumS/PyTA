#! /usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup

# To use this script, the user needs to provide the three values below: 
# myurl, myfilter, mydirectory
# Please make sure `mydirectory` is already created before running

myurl = "http://myurl.htm"
myfilter = "http://directory/"
mydirectory = "/extant/directory/"

myconnection = urllib.request.urlopen(myurl)
myhtml = myconnection.read()
mysoup = BeautifulSoup(myhtml, "lxml")
mylinks = mysoup.find_all('a')

all_links = []
for tag in mylinks:
    link = tag.get('href',None)
    if link is not None:
        all_links.append(link)

myresults = [k for k in all_links if myfilter in k]

for result in myresults:
    remotefile = urllib.request.urlopen(result)
    localfile = open(mydirectory+result.replace(myfilter, ''),'wb')
    localfile.write(remotefile.read())
    localfile.close()
    remotefile.close()