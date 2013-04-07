import urllib2
import re
import sys
try:
    try:
        url = sys.argv[1]
    except IndexError:
        url = raw_input("[dailymotion]  which file do you want to download?          ")
    if "http" not in url:
        url = "http://"+ url
    if "dailymotion.com" not in url:
        print "[dailymotion]  invalid url"
        sys.exit()
    print "[dailymotion]  got the url"
    print "[dailymotion]  loading webpage"
    html = urllib2.urlopen(url).read()
    print "[dailymotion]  page loaded"
    line = re.sub("%22",'"',html)
    line = re.sub("%7D","}",line)
    line = re.sub("%2C",",",line)
    line = re.sub("%7B","{",line)
    line = re.sub("%3A",":",line)
    line = re.sub("%5D","]",line)
    line = re.sub("%2F","/",line)
    line = re.sub("%5C","",line)
    line = re.sub("%3F","?",line)
    line = re.sub("%3D","=",line)
    line = re.sub("%2B","+",line)
    line = re.sub("%25","%",line)
    line = re.sub("%3E",">",line)
    line = re.sub("%3C","<",line)
    for key in ['hd1080URL', 'hd720URL', 'hqURL', 'sdURL', 'ldURL', 'video_url']:
        if key in html:
            max_quality = key
            print u'[dailymotion]  using %s' % key
            break
        else:
            #print u'unable to extract video URL'
            pass
            
    abc = re.search(r'"' + max_quality + r'":"(.+?)"', line)
    print "[dailymotion]  " + abc.group(1)
except urllib2.URLError:
    print "[dailymotion]  invalid url"
    sys.exit()
