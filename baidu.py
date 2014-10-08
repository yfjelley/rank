# -*- coding:utf-8 -*-
import sys
reload(sys).setdefaultencoding("utf8")
import urllib,urllib2,threading,re
import BeautifulSoup

class threadScrapy(threading.Thread):
    def __init__(self,url,num):
        threading.Thread.__init__(self)
        self.url = url
        self.thread_num = num
        self.thread_stop = False

    def run(self):
        print self.url
        print self.thread_num
        html = urllib.urlopen(self.url)
        soup = BeautifulSoup.BeautifulSoup(html)
        l = soup.html.body.find('div' ,id='content_left').findAll('span',{'class':re.compile('^\w{5,7}$')})
        print len(l)
        print l
        #l=filter(lambda x : '-' not in str(x),l)
        parten = re.compile(r'\<span\s{1}class\=\"\w{3,6}"\>(.+*)\<\/span\>')
        for i in l:
            match=parten.match(str(i))
            if match :
                print match.group(1)
        #l = soup.findAll(attrs={"class":'VJDfES'})
        with open('html.txt','w') as f:
            f.write(str(l).strip().strip("@"))

    def stop(self):
        self.thread_stop = True

if __name__ == "__main__" :
    url = "http://www.baidu.com/s?wd=不孕不育"
    x=threadScrapy(url,1)
    x.start()


    '''
    for i in range(3000):
        url = "http://www.baidu.com/s?wd=%d"%i
        x="t"+bytes(i)
        x=threadScrapy(url,i)
        x.start()
    '''



