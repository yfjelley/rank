# -*- coding:utf-8 -*-
import sys ,urllib,time,re

# Import Qt GUI component
from PyQt4 import QtGui 
from PyQt4 import QtCore
from PyQt4.QtWebKit import *
from PyQt4.Qt import *
from pyquery import PyQuery as pq

# Import GUI File
from ui_rank import Ui_MainWindow

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Make main window class
class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.webView=QWebView()
        self.model = QStandardItemModel(10, 3, self.tableView)
        self.model.setHorizontalHeaderLabels([u'关键字', u'地区', u'医院'])

    def _readRank(self):
    	with open('rank.txt') as f:
    	    for line in f.readlines():
    	    	yield line

    def _loadUrl(self):
        self.url="http://www.baidu.com/s?wd=%s+%s"%(self.keyWord,self.addres)
        print self.url
        self.webView.load(QUrl(self.url))
        self.webView.show()
        time.sleep(1)
        self.html = self.webView.page().mainFrame().toHtml()
        d = pq(str(self.html))
        x = d('.pagelist-name').text().strip().encode('utf-8')
        print x
        #reg = re.compile(r'【.*?】',re.X)
        self.parten = re.split(r'【.*?】',x)#【不孕不育】
        print self.parten
    def _showTable(self,parten):    	
        for i in parten:
            if len(i)>3:
               print i               
               self.model.setData(self.model.index(parten.index(i)-1, 0, QModelIndex()), QVariant(unicode(self.addres)))
               self.model.setData(self.model.index(parten.index(i)-1, 1, QModelIndex()), QVariant(unicode(self.keyWord)))
               self.model.setData(self.model.index(parten.index(i)-1, 2, QModelIndex()), QVariant(i.decode('utf-8')))
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setWindowTitle('Grid + Combo Testing')
        self.tableView.show()
    def main(self):
    	r = self._readRank()
    	for line in r:
    	    p = line.split()
            if len(p) == 4:
               self.keyWord,self.addres,self.hospital,self.rank = map(lambda x:unicode(x),p)
               self._loadUrl()
               self._showTable(self.parten)
               time.sleep(2)
        else:
            return 
    def show(self):
        self._showTable(self.parten)
        super(MainWindow,self).show()

                  
if __name__ == '__main__':
    Program = QtGui.QApplication(sys.argv)
    Window=MainWindow()
    Window.main()
    Window.show()
  

    Program.exec_()
    

