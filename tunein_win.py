#!/usr/bin/python
# encoding: utf-8
import os,sys
import PyInquirer
import untangle
import requests
import webbrowser
import platform

reload(sys)
sys.setdefaultencoding('Cp1254')
#If you want to use the program using an alias
#uncomment the following line and write your correct path
#os.chdir("C:\\Users\\user\\tunein-cli")
type={}
station={}
headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:74.0) Gecko/20100101 Firefox/74.0' }
source="http://opml.radiotime.com/Browse.ashx"

erase="cls"

#check mplayer
try:
    std=os.popen("mplayer").read()
    if len(std) == 0:
        raise
except:
    print underline('\nmplayer is not installed\nPlease install mplayer first.')
    exit()

def get(url,s):
    page = requests.get(url)
    xml=page.content
    if s=="true":
        obj = untangle.parse(xml)
        return obj
    else:
        return xml

def scrape(url,keyword):
    if url=="":
        url=source
    os.system(erase)
    out=['<<back']
    dup_out=['<<back']
    type={}
    station={}
    obj=get(url,"true")
    if keyword!="":
        stream=get(url,"true")
        if dir(stream.opml.body.outline).count("outline")>2:
            for i in obj.opml.body.outline.outline:
                type[i["text"]]=i["URL"]
        else:
            if isinstance(keyword, int)==True:
                target=keyword
            else:
                for i in stream.opml.body.outline:
                    if i['key'] == keyword:
                        target=stream.opml.body.outline.index(i)
            for i in obj.opml.body.outline[target].outline:
                type[i["text"]]=i["URL"]
    else:
        for i in obj.opml.body.outline:
            type[i["text"]]=i["URL"]
    a=1
    for i in type.keys():
        if i.strip() == "More Stations":
            st1="[%s] " %(a)
            st2=i
            out.insert(1,"%s%s" %(st1,st2))
            dup_out.insert(1,"%s%s" %(st1,st2))
        elif i.strip() == "Find by Name":
            st1="[%s] " %(a)
            st2=i
            out.insert(2,"%s%s" %(st1,st2))
            dup_out.insert(2,"%s%s" %(st1,st2))
        else:
            st1="[%s] " %(a)
            st2="".join(i)
            out.append("%s%s" %(st1,st2))
            dup_out.append("%s%s" %(st1,st2))
        a+=1
    ask=[
        {'type':'list',
         'name':'opt',
         'message':'Choose',
         'choices':out
        }
        ]
    ans=PyInquirer.prompt(ask)['opt']
    if ans == "<<back":
        main()
    else:
        choice=int(dup_out[out.index(ans)].split()[0][1:-1])
    choice-=1
    st_url=type[type.keys()[choice]]
    if st_url != None and "Tune.ashx?id" in st_url:
        st_title=type.keys()[choice]
        newurl=get(st_url,"false")
        if len(newurl.split())>1:
          newurl=newurl.split()[0]
        playlist(newurl,st_title)
    if st_url==None:
        tt=dup_out[out.index(ans)].split()
        tt.remove(dup_out[out.index(ans)].split()[0])
        for i in obj.opml.body.outline:
            if i["text"]==" ".join(tt):
              key=i["key"]
              if key==None:
                key=choice
        #print "SCRAPE:",url,key
        scrape(url,key)
    scrape(st_url,"")

def playlist(url,title):
    global run
    print "\nTitle:",u''.join(title).encode("cp1254")
    print "STREAM:",url
    if ".pls" in url:
        print "pls file found"
        url=os.popen("python getter.py '%s false'" %(url.strip())).read()[6:]
        print "FOUND:",url
    if run=="true":
        print "Opening stream..."
        print "To stop streaming press enter:"
        os.system("mplayer -really-quiet %s" %(url))
        print ""
        kill=raw_input("exit:")
        os.system("pkill -9 mplayer")
        main()
    elif run == "false":
        try:
            title.encode('ascii')
            new_title=title
            if new_title.startswith(".")==True:
                new_title=new_title[1:]
        except UnicodeEncodeError:
            new_title="".join(x for x in title if x.isalnum())
            if new_title.startswith(".")==True:
                new_title=new_title[1:]
            new_title=new_title.encode('cp1254')
        #title="playlist"
        file=open("%s.pls" %(new_title),"w")
        file.write("[playlist]")
        file.write("\nFile1=%s" %(url.strip()))
        file.write("\nTitle1=%s" %(r''.join(new_title)))
        file.write("\nLength1=-1")
        file.write("\nNumberOfEntries=1")
        file.write("\nVersion=2")
        file.close()
        print "Location: "+os.path.abspath("%s.pls" %(new_title))
        print "done."
        exit()
    elif run == "info":
        exit()
    elif run == "browser":
        print "Opening stream in browser..."
        webbrowser.get('windows-default').open(url)
        main()
    elif run == "fav":
        fav=open("fav_st.txt","a+")
        fav.write("%s %s" %(u''.join(title).encode("cp1254"),url))
        fav.close()
        print "added.\npress enter to continue:", raw_input()
        main()

#START from HERE
def main():
    global run
    run="false"
    os.system(erase)
    ask1=[
        {'type':'list',
         'name':'opt',
         'message':'Select Option',
         'choices':[
            '[1]: Open Stream',
            '[2]: Download Stream',
            '[3]: Show Stream Source',
            '[4]: Open In Browser',
            '[5]: Add to Favourites',
            '[6]: Add custom station',
            '[7]: Favourites',
            '[8]: Exit']
        }
    ]
    ans1=PyInquirer.prompt(ask1)['opt']
    if ans1[1:2] == "1":
        run="true"
    elif ans1[1:2] == "2":
        run="false"
    elif ans1[1:2] == "3":
        run="info"
    elif ans1[1:2] == "4":
        run="browser"
    elif ans1[1:2] == "5":
        run="fav"
    elif ans1[1:2] == "6":
        c_name=raw_input("Name:")
        c_url=raw_input("Address:")
        fav=open("fav_st.txt","a+")
        fav.write("%s %s" %(u''.join(c_name).encode("cp1254"),c_url))
        fav.close()
        print "added.\npress enter to continue:", raw_input()
        main()
    elif ans1[1:2] == "7":
        favlist={}
        dupfavlist=["<<back"]
        dup2favlist=["<<back"]
        fav=open("fav_st.txt","r").read().splitlines()
        for item in fav:
            if len(item)!=0:
                favlist[" ".join(item.split()[0:-1])]=item.split()[-1]
                dupfavlist.append(" ".join(item.split()[0:-1]))
                dup2favlist.append(" ".join(item.split()[0:-1]))
        os.system(erase)
        ask2=[
            {'type':'list',
             'name':'opt',
             'message':'Choose:',
             'choices':dup2favlist
            }
        ]
        ans2=PyInquirer.prompt(ask2)['opt']
        if ans2 == "<<back":
            main()
        run="true"
        playlist(favlist[dupfavlist[dup2favlist.index(ans2)]],ans2.encode("cp1254"))
    elif ans1[1:2] == "8":
        print "Bye."
        exit()
    scrape("","")
main()
