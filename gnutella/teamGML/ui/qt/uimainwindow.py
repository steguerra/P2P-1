# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Apr 13 12:40:18 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 40, 291, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 611, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.searchNeighboursBtn = QtGui.QPushButton(self.tab)
        self.searchNeighboursBtn.setGeometry(QtCore.QRect(440, 20, 161, 32))
        self.searchNeighboursBtn.setObjectName(_fromUtf8("searchNeighboursBtn"))
        self.peerIP = QtGui.QLineEdit(self.tab)
        self.peerIP.setGeometry(QtCore.QRect(60, 300, 181, 22))
        self.peerIP.setText(_fromUtf8(""))
        self.peerIP.setObjectName(_fromUtf8("peerIP"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 62, 22))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(250, 300, 62, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.peerPort = QtGui.QLineEdit(self.tab)
        self.peerPort.setGeometry(QtCore.QRect(320, 300, 61, 22))
        self.peerPort.setText(_fromUtf8(""))
        self.peerPort.setObjectName(_fromUtf8("peerPort"))
        self.addPeerBtn = QtGui.QPushButton(self.tab)
        self.addPeerBtn.setGeometry(QtCore.QRect(440, 297, 161, 32))
        self.addPeerBtn.setObjectName(_fromUtf8("addPeerBtn"))
        self.peersTreeWidget = QtGui.QTreeWidget(self.tab)
        self.peersTreeWidget.setGeometry(QtCore.QRect(10, 50, 584, 221))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peersTreeWidget.sizePolicy().hasHeightForWidth())
        self.peersTreeWidget.setSizePolicy(sizePolicy)
        self.peersTreeWidget.setItemsExpandable(False)
        self.peersTreeWidget.setObjectName(_fromUtf8("peersTreeWidget"))
        self.peersTreeWidget.header().setVisible(False)
        self.peersTreeWidget.header().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.sharedFilesListWidget = QtGui.QListWidget(self.tab_2)
        self.sharedFilesListWidget.setGeometry(QtCore.QRect(10, 20, 581, 301))
        self.sharedFilesListWidget.setObjectName(_fromUtf8("sharedFilesListWidget"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.uploadsTreeWidget = QtGui.QTreeWidget(self.tab_3)
        self.uploadsTreeWidget.setGeometry(QtCore.QRect(10, 200, 581, 121))
        self.uploadsTreeWidget.setObjectName(_fromUtf8("uploadsTreeWidget"))
        self.downloadsTreeWidget = QtGui.QTreeWidget(self.tab_3)
        self.downloadsTreeWidget.setGeometry(QtCore.QRect(10, 30, 581, 141))
        self.downloadsTreeWidget.setObjectName(_fromUtf8("downloadsTreeWidget"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.searchLineEdit = QtGui.QLineEdit(self.tab_4)
        self.searchLineEdit.setGeometry(QtCore.QRect(160, 20, 321, 22))
        self.searchLineEdit.setObjectName(_fromUtf8("searchLineEdit"))
        self.searchBtn = QtGui.QPushButton(self.tab_4)
        self.searchBtn.setGeometry(QtCore.QRect(490, 20, 101, 21))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.resultsTreeWidget = QtGui.QTreeWidget(self.tab_4)
        self.resultsTreeWidget.setGeometry(QtCore.QRect(10, 70, 581, 231))
        self.resultsTreeWidget.setObjectName(_fromUtf8("resultsTreeWidget"))
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Gnutella client", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "by Ferrari Luca, Bersani Marco, Lodi Giovanni", None, QtGui.QApplication.UnicodeUTF8))
        self.searchNeighboursBtn.setText(QtGui.QApplication.translate("MainWindow", "Search neighbours", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Peer IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Peer port", None, QtGui.QApplication.UnicodeUTF8))
        self.addPeerBtn.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.peersTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Peer IP", None, QtGui.QApplication.UnicodeUTF8))
        self.peersTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Peer Port", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Neighbours", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Shared files", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Downloads:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Uploads:", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadsTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Percentage", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadsTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Peer", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadsTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Md5", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadsTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Percentage", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadsTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Peer", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadsTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Md5", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Transfers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "File name to search:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBtn.setText(QtGui.QApplication.translate("MainWindow", "Search!", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Peer IP", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Peer port", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Md5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Double click on a file to download it", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))

