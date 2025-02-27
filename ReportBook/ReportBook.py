

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class RP_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(767, 555)
        self.labelTron = QtWidgets.QLabel(Dialog)
        self.labelTron.setGeometry(QtCore.QRect(10, 20, 391, 231))
        self.labelTron.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelTron.setObjectName("labelTron")
        self.labelCot = QtWidgets.QLabel(Dialog)
        self.labelCot.setGeometry(QtCore.QRect(10, 290, 391, 231))
        self.labelCot.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelCot.setObjectName("labelCot")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 30, 311, 491))
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ReportDialog"))
        self.labelTron.setText(_translate("Dialog", "Hình tròn"))
        self.labelCot.setText(_translate("Dialog", "Hình cột"))
        self.label_3.setText(_translate("Dialog", "Thông tin"))





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RP_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())