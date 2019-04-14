#WORKS WITH 2.X
import os
import sys
from pytube import YouTube
import re
islist = True
cow = False
if not os.path.exists("./mp4"):
    os.system('mkdir mp4')
if not os.path.isfile("./list.txt"):
    os.system('touch list.txt')
linkdon = 1
linknum = 0

def checkargs():
    global islist
    global linkdon
    for arg in sys.argv:
        print arg
        if re.match('^cow$', arg):
            cow=True
    for arg in sys.argv:
        if re.match('.*[0-9A-Za-z_-]{11}', arg):
            islist=False
            prep_link(arg)
            down_link(prepared)
            linkdon += 1

def load_links():
    global linkek
    global linknum
    txt = open("list.txt", "r")
    linkek = txt.read().split('\n')
    linknum = len(linkek)-1
    linkek.pop(linknum)

def verbose(progress):
    global linknum
    if not islist:
        linknum = '?'
    msg = "Downloading video "+progress+"..."+"("+str(linkdon)+"/"+str(linknum)+")"
    if cow:
        os.system('clear')
        os.system('cowsay "' + msg + '"')
    else:
        print msg
        
def prep_link(raw):
    global prepared
    linkid = re.search('[0-9A-Za-z_-]{11}', raw.strip()).group(0)
    prepared = "youtu.be/" + linkid
    verbose(linkid)

def down_link(prepped):
    YouTube(prepped).streams.first().download('./mp4/')

checkargs()

if islist:     
    load_links()
    for x in linkek:
        prep_link(x)
        down_link(prepared)
        linkdon += 1
if cow:
    os.system('clear')


