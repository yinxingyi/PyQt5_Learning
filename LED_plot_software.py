import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QAction, qApp, QMenu
from PyQt5.QtWidgets import (QLabel, QInputDialog)
from PyQt5.QtGui import QIcon

class Main_page(QMainWindow):

    def __init__(self):
        super(Main_page, self). __init__()
        self.InitUI()

    def InitUI(self):


        self.setGeometry(300,300,700,600)
        self.setWindowTitle('LED Selector')
        self.setWindowIcon(QIcon('Nidec.png'))
        self.statusBar().showMessage('Ready')

        exitAct = QAction(QIcon('Exit.png'),'Exit(&E)',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit program')
        exitAct.triggered.connect(qApp.quit)

        newAct = QAction(QIcon('new.png'),'New File(&N)',self)
        newAct.setStatusTip('Create a New File')
        newAct.setShortcut('Ctrl+N')

        openFileAct = QAction(QIcon('Openfile.png'),'Open File(&O)',self)
        openFileAct.setShortcut('Ctrl+O')
        openFileAct.setStatusTip('Open a File')
        openFileAct.triggered.connect(qApp.quit)

        saveMenu = QMenu('SAVE(&S)',self)
        saveFileAct = QAction(QIcon('SaveFile.png'),'Save File(&S',self)
        saveFileAct.setShortcut('Ctrl+S')
        saveFileAct.setStatusTip('Save a file')
        saveFileAct.triggered.connect(qApp.quit)
        saveasAct = QAction(QIcon('SaveAs.png'),'Save as...(&A)',self)
        saveasAct.setStatusTip('Save a file as')
        saveMenu.addAction(saveFileAct)
        saveMenu.addAction(saveasAct)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addAction(openFileAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('TOOL')
        toolbar.addAction(newAct)
        toolbar.addAction(openFileAct)
        toolbar.addAction(saveFileAct)
        toolbar.addAction(saveasAct)
        toolbar.addAction(exitAct)



        self.bt1 = QPushButton('FORD WHITE', self)
        self.bt1.move(50,90)
        self.bt1.setStatusTip('Ford Lincoln White')
        self.bt1.setToolTip('<b> click here to open Ford White Spec</b>')
        self.bt1.clicked.connect(self.Spec_ford_white)

        self.bt2 = QPushButton('FORD IceBlue', self)
        self.bt2.move(50, 140)
        self.bt2.setStatusTip('Ford Ice Blue')
        self.bt2.setToolTip('<b> click here to open Ford IceBlue Spec</b>')
        self.bt2.clicked.connect(self.Spec_Ford_IceBlue)

        self.bt3 = QPushButton('FORD Yellow', self)
        self.bt3.move(50, 190)
        self.bt3.setStatusTip('Ford Yellow')
        self.bt3.setToolTip('<b> click here to open Ford Yellow Spec</b>')
        self.bt3.clicked.connect(self.Spec_Ford_Yellow)

        self.bt4 = QPushButton('ALL Spec', self)
        self.bt4.move(50, 240)
        self.bt4.setStatusTip('Open All Ford Color SPECs')
        self.bt4.setToolTip('<b> click here to open All Spec</b>')
        self.bt4.clicked.connect(self.Spec_Ford_All)


        self.bt_LED_Enter = QPushButton('New LED Enter', self)
        self.bt_LED_Enter.move(200,90)
        self.bt_LED_Enter.setStatusTip('<b> Click to open New LED Enter')
        self.bt_LED_Enter.clicked.connect(self.Open_LED_Enter)

        self.show()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        openAct = cmenu.addAction('Save')
        quitAct = cmenu.addAction('Quit')

        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def Open_LED_Enter(self):

        Open_En = QMainWindow(self)
        Open_En.setGeometry(400,400,500,800)
        Open_En.setWindowTitle('LED Enter')


        Open_En.show()


        # Open_LED_EN = LED_enter()
        #
        # Open_LED_EN.show()

        # # Open_LED_EN.setModal(True)
        # # Open_LED_EN.exec()


    def Spec_ford_white(self):

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.scatter(0.340, 0.340, marker = 'o')
        ax.scatter(0.330, 0.336, marker='x')

        datax = [0.355, 0.354, 0.353, 0.351, 0.350, 0.349, 0.347, 0.346, 0.344, 0.343, 0.341, 0.339, 0.338, 0.336,
                 0.334, 0.333, 0.331, 0.330, 0.328, 0.327, 0.325, 0.324, 0.323, 0.322, 0.321, 0.320, 0.320, 0.319,
                 0.319, 0.319, 0.319, 0.319, 0.319, 0.319, 0.320, 0.321, 0.321, 0.322, 0.323, 0.325, 0.326, 0.327,
                 0.329, 0.330, 0.332, 0.333, 0.335, 0.337, 0.338, 0.340, 0.342, 0.343, 0.345, 0.346, 0.348, 0.349,
                 0.351, 0.352, 0.353, 0.354, 0.355, 0.356, 0.356, 0.357, 0.357, 0.357, 0.357, 0.357, 0.357, 0.357,
                 0.356, 0.355, 0.355]
        datay = [0.356, 0.357, 0.357, 0.357, 0.357, 0.356, 0.356, 0.355, 0.355, 0.354, 0.353, 0.351, 0.350, 0.349,
                 0.347, 0.346, 0.344, 0.342, 0.340, 0.338, 0.336, 0.335, 0.333, 0.331, 0.329, 0.327, 0.325, 0.324,
                 0.322, 0.321, 0.319, 0.318, 0.317, 0.316, 0.315, 0.314, 0.314, 0.313, 0.313, 0.313, 0.313, 0.314,
                 0.314, 0.315, 0.315, 0.316, 0.317, 0.319, 0.320, 0.321, 0.323, 0.324, 0.326, 0.328, 0.330, 0.332,
                 0.334, 0.335, 0.337, 0.339, 0.341, 0.343, 0.345, 0.346, 0.348, 0.349, 0.351, 0.352, 0.353, 0.354,
                 0.355, 0.356, 0.356]

        ax.plot(datax, datay, color='k', linestyle='-', linewidth=2, label= 'Lincoln White')
        # plt.axis([0,1,0,1])  # to make scral at X:0,1,Y:0,1
        plt.suptitle('Ford Lincoln White')
        plt.legend(["Ford Lincoln White","measurement1","measurement2"], loc=0)
        plt.xlabel('Cx')
        plt.ylabel('Cy')
        plt.grid(True)
        plt.show()

    def Spec_Ford_IceBlue(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        datax = [0.168, 0.1791, 0.2077, 0.1956, 0.168]
        datay = [0.2527, 0.3, 0.3, 0.2504, 0.2527]

        ax.plot(datax, datay, color='b', linestyle='-', linewidth=2 , marker = 'o', label = 'Ford IceBlue')
        ax.scatter([0.1818, 0.1957, 0.1826, 0.2020, 0.1843, 0.2013], [0.2543, 0.2785, 0.2560, 0.2907, 0.2611, 0.2890],marker = 'x')
        plt.xlabel('Cx')
        plt.ylabel('Cy')
        plt.suptitle('Ford Ice Blue')
        plt.legend(["Ford Ice Blue","measurement"], loc=0)
        plt.grid(True)
        plt.show()

    def Spec_Ford_Yellow(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        datax = [0.509, 0.509, 0.591, 0.509]
        datay = [0.408, 0.49, 0.408, 0.408]

        ax.plot(datax, datay, color='y', linestyle='-', linewidth=2)
        plt.xlabel('Cx')      #X轴名称
        plt.ylabel('Cy')      #Y轴名称
        plt.suptitle('Ford yellow') #标题
        plt.legend(["Ford Yellow","measurement"], loc = 0) #图例，图例中的 loc 参数标记图例位置，
                                                        # 1，2，3，4 依次代表：右上角、左上角、左下角，右下角；0 代表自适应

        plt.grid(True)
        plt.show()

    def Spec_Ford_All(self):


        fig = plt.figure()
        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)


        datax_w = [0.355, 0.354, 0.353, 0.351, 0.350, 0.349, 0.347, 0.346, 0.344, 0.343, 0.341, 0.339, 0.338, 0.336,
                 0.334, 0.333, 0.331, 0.330, 0.328, 0.327, 0.325, 0.324, 0.323, 0.322, 0.321, 0.320, 0.320, 0.319,
                 0.319, 0.319, 0.319, 0.319, 0.319, 0.319, 0.320, 0.321, 0.321, 0.322, 0.323, 0.325, 0.326, 0.327,
                 0.329, 0.330, 0.332, 0.333, 0.335, 0.337, 0.338, 0.340, 0.342, 0.343, 0.345, 0.346, 0.348, 0.349,
                 0.351, 0.352, 0.353, 0.354, 0.355, 0.356, 0.356, 0.357, 0.357, 0.357, 0.357, 0.357, 0.357, 0.357,
                 0.356, 0.355, 0.355]
        datay_w = [0.356, 0.357, 0.357, 0.357, 0.357, 0.356, 0.356, 0.355, 0.355, 0.354, 0.353, 0.351, 0.350, 0.349,
                 0.347, 0.346, 0.344, 0.342, 0.340, 0.338, 0.336, 0.335, 0.333, 0.331, 0.329, 0.327, 0.325, 0.324,
                 0.322, 0.321, 0.319, 0.318, 0.317, 0.316, 0.315, 0.314, 0.314, 0.313, 0.313, 0.313, 0.313, 0.314,
                 0.314, 0.315, 0.315, 0.316, 0.317, 0.319, 0.320, 0.321, 0.323, 0.324, 0.326, 0.328, 0.330, 0.332,
                 0.334, 0.335, 0.337, 0.339, 0.341, 0.343, 0.345, 0.346, 0.348, 0.349, 0.351, 0.352, 0.353, 0.354,
                 0.355, 0.356, 0.356]

        datax_b = [0.168, 0.1791, 0.2077, 0.1956, 0.168]
        datay_b = [0.2527, 0.3, 0.3, 0.2504, 0.2527]

        datax_y = [0.509, 0.509, 0.591, 0.509]
        datay_y = [0.408, 0.49, 0.408, 0.408]

        ax1.plot(datax_w, datay_w, color='r', linestyle='-', linewidth=2)
        ax2.plot(datax_b, datay_b, color='b', linestyle='-', linewidth=2, marker='o', label='Ford IceBlue')
        ax3.plot(datax_y,datay_y, color = 'y', linestyle='-', linewidth = 2, marker = 'o', label = 'Ford Yellow')

        plt.grid(True)

        plt.show()

# class LED_enter(QMainWindow):
#
#     def __init__(self):
#
#         super().__init__()
#
#         self.LED_EN()
#
#     def LED_EN(self):
#
#         self.setGeometry(400,400,500,800)
#         self.setWindowTitle('New LED Enter')
#         self.setWindowIcon(QIcon('Omron.png'))
#
#         self.show()


if __name__ == "__main__":


    app = QApplication(sys.argv)
    main = Main_page()

    sys.exit(app.exec_())


