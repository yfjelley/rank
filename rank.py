# -*- coding:utf-8 -*-
import sys
reload(sys).setdefaultencoding("utf8")
import urllib,urllib2,threading,re
import BeautifulSoup
import MySQLdb

try:
    '''
    create database 
    '''
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123')
    cursor = conn.cursor()
    sql= '''create database if not exists `baidu` default character set utf8 collate utf8_general_ci;'''
    cursor.execute(sql)
    conn.select_db('baidu')
    cursor.execute('''drop table if exists alex;''')
    sql='''create table if not exists alex(`keyword` varchar(100),`addres` varchar(100),`site` varchar(100),`rank` int(3))ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    cursor.execute(sql)
except Exception,e:
    print e
def writeData(sql):
    '''
    insert data into table
    '''
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123',db='baidu')
        cursor = conn.cursor()
        cursor.execute(sql)
        print sql
        cursor.close()
    except Exception,e:
        print e
        print sql
        pass

class threadScrapy(threading.Thread):
    def __init__(self,kw,num):
        threading.Thread.__init__(self)
        self.keyWord = kw
        self.addres = '上海'
        self.url = "http://www.baidu.com/s?wd=%s%s%s"%(self.keyWord,urllib.quote('+'),'上海')
        self.thread_num = num
        self.thread_stop = False


    def run(self):
        print self.url,self.thread_num
        html = urllib.urlopen(self.url)
        soup = BeautifulSoup.BeautifulSoup(html)
        #l = soup.html.body.find('div',id='content_left').findAll('span',{'class':re.compile('^\w{5,7}$')})
        l = soup.html.body.find('div',id='content_left').findAll('span',{'class':'g'})
        parten = re.compile(r'\<span\s{1}class\=\"g"\>(.+?)\;(.+?)\<\/span\>')
        for i in l:
            match=parten.match(str(i))
            if match :
                writeData('''insert into alex values('%s','%s','%s',%d);'''%(self.keyWord,self.addres,match.group(1),l.index(i)))
        #l = soup.findAll(attrs={"class":'VJDfES'})

    def stop(self):
        self.thread_stop = True

if __name__ == "__main__" :
    keyWord = "不孕不育"
    x=threadScrapy(keyWord,1)
    x.start()

