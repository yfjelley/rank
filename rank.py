#-*- coding:utf-8 -*-
import sys,time,re
reload(sys).setdefaultencoding("utf8")
from PyQt4 import QtGui,QtCore,QtSql,QtXml
from PyQt4.QtWebKit import *
from PyQt4.Qt import *
from pyquery import PyQuery as pq
class Test(QtGui.QWidget):
	#sin = pyqtSignal()
    def __init__(self,parent=None):
        self.app=QtGui.QApplication([])
        super(Test,self).__init__(parent)
        self.webView=QWebView()
        
        self.setGeometry(342,231,454,388)
        self.layvTop=QtGui.QVBoxLayout()
        self.setLayout(self.layvTop)
            
        self.txt=QtGui.QTextEdit()
        self.layvTop.addWidget(self.txt)
        self.timer=QtCore.QTimer()
        QtCore.QObject.connect(self.timer,QtCore.SIGNAL("timeout()"), self.OnTimer)
        self.timer.start( 1000 )
    def write(self,txt):
        self.txt.textCursor().insertText(txt)
    def show(self):
        super(Test,self).show()
        self.app.exec_()

    def OnTimer(self,event=False):
        with open('rank.txt') as f:
           for line in f.readlines():
              p = line.split()
              if len(p) == 4:
                  keyWord,addres,hospital,rank = map(lambda x:unicode(x),p)
                  self.url="http://www.baidu.com/s?wd=%s+%s"%(keyWord,addres)
                  print self.url
                  #self.webView.load(QUrl(url))
                  self.webView.load(QUrl(self.url))
                  #self.webView.show()   
                  time.sleep(0.4)     
                  html = self.webView.page().mainFrame().toHtml()
                  d = pq(str(html))
                  x = d('.pagelist-name').text().strip()
                  reg = re.compile(u'【.*?】',re.X)
                  parten = reg.split(x)
                  print parten
                  #if len(parten) >1:
                  for i in parten:
                  	  print i
                  	  print "888"
                      #print keyWord,addres,i,parten.index(i)
              else:
              	  return
              time.sleep(3)
        
if __name__=='__main__':
    t=Test()
    sys.stdout=t
    t.show()
