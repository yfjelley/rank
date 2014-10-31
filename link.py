# -*- coding:utf-8 -*-
import sys,re,urllib,threading
from pyquery import PyQuery as pq
reload(sys).setdefaultencoding('utf-8')
class threadLink(threading.Thread):
    def __init__(self,kw,ft):
       threading.Thread.__init__(self)
       self.thread_stop = False
       self.kw=kw
       self.ft=ft
       self.d = pq("http://www.baidu.com/s?wd=%s"%self.kw)
       self.link = self.d('a[data-nolog]')
    def run(self):
       for i in self.link:
             href = self.d(i).attr('href')
             print href
             h=urllib.urlopen('%s'%href).read()
             html = h.decode('gb18030').encode('utf8')
             #print html
             m = re.search(r'%s'%self.ft,str(html))
             if m:
                 print self.kw,self.ft,self.link.index(i)
       for i in range(len(self.d('.result.c-container'))):
            x=self.d('.result.c-container:eq(%d)'%i).text()
            print x
            m=re.search(r'%s'%self.ft,str(x))
            if m:
                print "xxxx"
if __name__== "__main__":
    kw="上海不孕不育检查"
    ft="长江医院"
    th=threadLink(kw,ft)
    th.start()

         
        


        
        
