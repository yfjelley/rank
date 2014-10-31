# -*- coding:utf-8 -*-
import sys,re,urllib,threading
from pyquery import PyQuery as pq
reload(sys).setdefaultencoding('utf-8')
def worker(kw,ft):
    d = pq("http://www.baidu.com/s?wd=%s"%kw)
    #获取百度快照链接
    link = d('a[data-nolog]')
    for i in range(len(d('.result.c-container'))):
        #提取搜索的页面标题，如果标题中没有特征码，则打开百度快照
        x=d('.result.c-container:eq(%d)'%i).text()
        print x
        m=re.search(r'%s'%ft,str(x))
        if m:
            print kw,ft,i
        else:
            href = d(link[i]).attr('href')
            print href
            #打开百度快照页
            h=urllib.urlopen('%s'%href).read()
            html = h.decode('gb18030').encode('utf8')
            #print html
            m = re.search(r'%s'%ft,str(html))
            if m:
                 print kw,ft,link.index(i)

if __name__== "__main__":
    kw="上海不孕不育检查"
    ft="长江医院"
 
    for i in xrange(100):
        while(1):
            if threading.activeCount() <3:
                try:
                    t = threading.Thread(target=worker,args=(kw,ft))
                    t.start()
                except Exception,e:
                    print e
                    pass
                break
             
        


        
        
