#!/usr/bin/python
#-*- encoding: utf-8 -*-
import os
import untangle
import requests
import sys
import curses

type={}
station={}
source="http://opml.radiotime.com/Browse.ashx?c=music"

ERASE_LINE = '\x1b[1J'
ERASE_ALL = '\x1b[g'
GO_HOME = '\x1b[H'
SCROLL = '\x1b[1000M'
sys.stdout.write(ERASE_LINE)
sys.stdout.write(GO_HOME)

class colors:
    HEADER = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    ENDC = '\033[0m'
    bold = '\033[1m'
    UNDERLINE = '\033[4m'

#check mplayer
try:
    std=os.popen("mplayer").read()
    if len(std) == 0:
        raise
except:
    print colors.UNDERLINE+'\nmplayer is not installed\nPlease install mplayer first'+colors.ENDC
    exit()
#end

def get(url,s):
    page = requests.get(url)
    xml=page.content
    if s=="true":
        obj = untangle.parse(xml)
        return obj
    else:
        return xml

def playlist(url,title):
    global run
    print "\nTitle:",colors.bold+title+colors.ENDC
    print "STREAM:",colors.bold+url+colors.ENDC
    if ".pls" in url:
        print "pls file found"
        content=get(url,"false")
        url=content.splitlines()[1][6:]
    if run=="true":
        print "Opening stream..."
        print "To stop streaming press enter"
        os.system("mplayer -really-quiet %s" %(url))
        print ""
        kill=raw_input("exit:")
        os.system("pkill -9 mplayer")
        exit()
    else:
        try:
            title.encode('ascii')
            new_title=title
            if new_title.startswith(".")==True:
                new_title=new_title[1:]
        except UnicodeEncodeError:
            new_title="".join(x for x in title if x.isalnum())
            if new_title.startswith(".")==True:
                new_title=new_title[1:]
            new_title=new_title.encode('utf8')
        #title="playlist"
        file=open("%s.pls" %(new_title),"w")
        file.write("[playlist]")
        file.write("\nFile1=%s" %(url.strip()))
        file.write("\nTitle1=%s" %(r''.join(new_title)))
        file.write("\nLength1=-1")
        file.write("\nNumberOfEntries=1")
        file.write("\nVersion=2")
        file.close()
        print "done"
        exit()

def typelist():
    out=[]
    obj=get(source,"true")
    for i in obj.opml.body.outline:
        type[i["text"]]=i["URL"]
    a=1
    print "Choose a type from the list:"
    for i in type.keys():
        st1=colors.red + "%s) " %(a) + colors.ENDC
        st2=colors.bold+i+colors.ENDC
        out.append("%s%s" %(st1,st2))
        a+=1
    sys.stdout.write("\r%s" %("\n".join(out)))
    choice=input("\nType:")
    choice-=1
    st_url=type[type.keys()[choice]]
    return st_url

def morelist(more):
    out=[]
    try:
        obj = untangle.parse(more)
    except:
        if more.startswith("http") == True:
            print "multiple URLs found\n",more
            playlist(more.splitlines()[0],"stream")
    for i in obj.opml.body.outline:
        station[i["text"]]=i["URL"]
    a=1
    for i in station.keys():
        if i.strip() == "More Stations":
            st1=colors.green + "%s) " %(a) + colors.ENDC
            st2=colors.green+i+colors.ENDC
            out.append("%s%s" %(st1,st2))
        else:
            st1=colors.red + "%s) " %(a) + colors.ENDC
            st2=colors.bold+i+colors.ENDC
            out.append("%s%s" %(st1,st2))
        a+=1
    os.system("clear && printf '\e[3J'")
    print "Choose a station from the list:"
    sys.stdout.write("\r%s" %("\n".join(out)))
    choice=input("\nStation:")
    choice-=1
    st_title=station.keys()[choice]
    st_url=station[station.keys()[choice]]
    newurl=get(st_url,"false")
    if newurl.count('\n') == 1:
        playlist(newurl,st_title)
        print "done"
        exit()
    else:
        morelist(newurl)

def stationlist(st_url):
    out=[]
    stream=get(st_url,"true")
    for i in stream.opml.body.outline[0].outline:
        station[i["text"]]=i["URL"]
    a=1
    for i in station.keys():
        if i.strip() == "More Stations":
            st1=colors.green + "%s) " %(a) + colors.ENDC
            st2=colors.green+i+colors.ENDC
            out.append("%s%s" %(st1,st2))
        else:
            st1=colors.red + "%s) " %(a) + colors.ENDC
            st2=colors.bold+i+colors.ENDC
            out.append("%s%s" %(st1,st2))
        a+=1
    os.system("clear && printf '\e[3J'")
    print "Choose a station from the list:"
    sys.stdout.write("\r%s" %("\n".join(out)))
    choice=input("\nStation:")
    choice-=1
    st_title=station.keys()[choice]
    st_url=station[station.keys()[choice]]
    newurl=get(st_url,"false")
    if newurl.count('\n') == 1:
        return newurl,st_title
    else:
        morelist(newurl)

#START from HERE
global run
run="false"
if raw_input("Do you want to open stream(y/n):") == "y":
    run="true"
st_url=typelist()
newurl,st_title=stationlist(st_url)
playlist(newurl,st_title)
