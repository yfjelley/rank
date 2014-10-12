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
        
        self.so()
    def readRank(self):
    	with open('rank.txt') as f:
    	    for line in f.readlines():
    	    	p = line.split('\s')
                self.so(p)

    def so(self,p):
        if len(p) == 4:
            keyWord,addres,hospital,rank = map(lambda x:unicode(x),p)
        else:
            return
        url="http://www.baidu.com/s?wd=%s+%s"%(keyWord,addres)
        self.webView.load(QUrl(url))
        #self.webView.show()
        time.sleep(2)
        html = self.webView.page().mainFrame().toHtml()
        d = pq(str(html))
        x = d('.pagelist-name').text().strip()
        x = x.encode('utf-8')
        reg = re.compile(r'【.*?】',re.X)
        parten = reg.split(x)#【不孕不育】
        model = QStandardItemModel(10, 3, self.tableView)
        model.setHorizontalHeaderLabels([u'关键字', u'地区', u'医院'])
        for i in parten:
            if len(i)>3:
               print parten.index(i)
               print i.decode("utf8")
               model.setData(model.index(parten.index(i)-1, 0, QModelIndex()), QVariant(u'%s'%addres))
               model.setData(model.index(parten.index(i)-1, 1, QModelIndex()), QVariant(u'%s'%keyWord))
               model.setData(model.index(parten.index(i)-1, 2, QModelIndex()), QVariant(i.decode('utf-8')))
        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setWindowTitle('Grid + Combo Testing')
        self.tableView.show()
          
if __name__ == '__main__':
    Program = QtGui.QApplication(sys.argv)
    Window=MainWindow()
    Window.show()
    Program.exec_()

