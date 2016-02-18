#-*- encoding: utf-8 -*-
import urllib
import urllib2
import re
import os

#下载网页中的图片等文件
def download(base, url):
    '''
    save css, js, img to folders respectively

    base:   base url for relative urls
    url:    url of the file

    return nothing
    '''
    if re.search('.+\.css',url,flags=re.I):
        filename='./css/'+url[url.rfind('/')+1:]
    elif re.search('.+\.js',url,flags=re.I):
        filename='./js/'+url[url.rfind('/')+1:]
    elif re.search('.+\.jpe?g|.+\.png|.+\.gif|.+\.svg',url,flags=re.I):
        filename='./images/'+url[url.rfind('/')+1:]
    else:
        print 'not a css, js, img:',url
        return
    if url.find('http://')<0:
        url=base+url
    urllib.urlretrieve(url,filename)

#获取网页
def getpage(url):
    '''
    get the web page

    url:    url of the web page

    return a string
    '''
    opener = urllib2.build_opener()
    opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'),
    ('Referer',url)]
    urllib2.install_opener(opener)
    return opener.open(url).read()

def backup(pageurl,dir):
    '''
    download a web page include the static resource

    pageurl:    url of the page

    return nothing
    '''
    cwd=os.getcwd()
    os.chdir(dir)
    try:
        os.mkdir('images')
        os.mkdir('js')
        os.mkdir('css')
    except:
        pass
    base=re.sub('(http://[\w\d\.\-/]+/)[^/]*$','\\1',pageurl,flags=re.I)
    html=getpage(pageurl)
    #图标和css
    src=re.findall('src="(.+?\..+?)"',html,flags=re.I)
    for url in src:
        download(base, url)
    #图片和脚本
    href=re.findall('href="([^"]+?\.[^"/]+?)"',html,flags=re.I)
    for url in href:
        download(base, url)
    #替换html中的地址
    html=re.sub('href="[\S]*/([^/]+\.jpe?g|[^/]+\.gif|[^/]+\.png|[^/]+\.svg)','href="./images/\\1"',html,flags=re.I)
    html=re.sub('href="[\S]*/([^/]+\.css)"','href="./css/\\1"',html,flags=re.I)
    html=re.sub('src="[\S]*/([^/]+\.jpe?g|[^/]+\.gif|[^/]+\.png)"','src="./images/\\1"',html,flags=re.I)
    html=re.sub('src="[\S]*/([^/]+\.js)"','src="./js/\\1"',html,flags=re.I)
    f=open('index.html','w')
    f.write(html)
    f.close()
    os.chdir(cwd)

if __name__=='__main__':
    backup('http://m.sohu.com/','images')
