#-*- encoding: utf-8 -*-
import urllib
import urllib2
import re
import os

#下载网页中的图片等文件
def download(url):
    if re.search('.+\.css',url,flags=re.I):
        filename='./css/'+url[url.rfind('/')+1:]
    elif re.search('.+\.js',url,flags=re.I):
        filename='./js/'+url[url.rfind('/')+1:]
    elif re.search('.+\.jpe?g|.+\.png|.+\.gif',url,flags=re.I):
        filename='./images/'+url[url.rfind('/')+1:]
    else:
        print 'not a css, js, img:',url
        return
    if url.find('http://')<0:
        url='http://m.sohu.com/'+url
    urllib.urlretrieve(url,filename)

#获取网页
def getpage(url):
    opener = urllib2.build_opener()
    opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'),
    ('Referer',url)]
    urllib2.install_opener(opener)
    return opener.open(url).read()

try:
    os.mkdir('images')
    os.mkdir('js')
    os.mkdir('css')
except:
    pass

html=getpage('http://m.sohu.com')
src=re.findall('src="(.+?\..+?)"',html,flags=re.I)
for url in src:
    download(url)

href=re.findall('href="([^"]+?\.[^"/]+?)"',html,flags=re.I)
for url in href:
    download(url)


html=re.sub('href="[\S]*/([^/]+\.jpe?g|[^/]+\.gif|[^/]+\.png)','href="./images/\\1"',html,flags=re.I)
html=re.sub('href="[\S]*/([^/]+\.css)"','href="./css/\\1"',html,flags=re.I)
html=re.sub('href="[\S]*/([^/]+\.js)','href="./js/\\1"',html,flags=re.I)

html=re.sub('src="[\S]*/([^/]+\.jpe?g|[^/]+\.gif|[^/]+\.png)"','src="./images/\\1"',html,flags=re.I)
html=re.sub('src="[\S]*/([^/]+\.css)"','src="./css/\\1"',html,flags=re.I)
html=re.sub('src="[\S]*/([^/]+\.js)"','src="./js/\\1"',html,flags=re.I)

f=open('index.html','w')
f.write(html)
f.close()
'''
        opener = urllib2.build_opener()
        opener.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'),
        #('Accept','image/png,image/*;q=0.8,*/*;q=0.5'),
        #('Accept-Language','zh-CN,en-US;q=0.7,en;q=0.3'),
        #('Accept-Encoding','gzip, deflate'),
        ('Referer',url)]
        urllib2.install_opener(opener)
        try:
            data = opener.open(url,timeout=5)
            f = open (filename,'wb')
            f.write(data.read())
            f.close()
        except:
            print 'error: %s' %url
'''