# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student_Grade(object):
    def setupUi(self, Student_Grade):
        Student_Grade.setObjectName("Student_Grade")
        Student_Grade.resize(733, 372)
        font = QtGui.QFont()
        font.setPointSize(10)
        Student_Grade.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Student_Grade)
        self.centralwidget.setObjectName("centralwidget")
        self.test1 = QtWidgets.QLabel(self.centralwidget)
        self.test1.setGeometry(QtCore.QRect(30, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test1.setFont(font)
        self.test1.setObjectName("test1")
        self.test2 = QtWidgets.QLabel(self.centralwidget)
        self.test2.setGeometry(QtCore.QRect(30, 190, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test2.setFont(font)
        self.test2.setObjectName("test2")
        self.test3 = QtWidgets.QLabel(self.centralwidget)
        self.test3.setGeometry(QtCore.QRect(30, 230, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test3.setFont(font)
        self.test3.setObjectName("test3")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(30, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.name_out = QtWidgets.QLineEdit(self.centralwidget)
        self.name_out.setGeometry(QtCore.QRect(110, 100, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_out.setFont(font)
        self.name_out.setObjectName("name_out")
        self.test1_out = QtWidgets.QLineEdit(self.centralwidget)
        self.test1_out.setGeometry(QtCore.QRect(110, 150, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test1_out.setFont(font)
        self.test1_out.setObjectName("test1_out")
        self.test2_out = QtWidgets.QLineEdit(self.centralwidget)
        self.test2_out.setGeometry(QtCore.QRect(110, 190, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test2_out.setFont(font)
        self.test2_out.setObjectName("test2_out")
        self.test3_out = QtWidgets.QLineEdit(self.centralwidget)
        self.test3_out.setGeometry(QtCore.QRect(110, 230, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test3_out.setFont(font)
        self.test3_out.setObjectName("test3_out")
        self.semester1 = QtWidgets.QRadioButton(self.centralwidget)
        self.semester1.setGeometry(QtCore.QRect(30, 260, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.semester1.setFont(font)
        self.semester1.setObjectName("semester1")
        self.semester2 = QtWidgets.QRadioButton(self.centralwidget)
        self.semester2.setGeometry(QtCore.QRect(30, 290, 91, 17))
        self.semester2.setObjectName("semester2")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(130, 262, 91, 41))
        self.submit.setObjectName("submit")
        self.student1 = QtWidgets.QLabel(self.centralwidget)
        self.student1.setGeometry(QtCore.QRect(260, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student1.setFont(font)
        self.student1.setObjectName("student1")
        self.student2 = QtWidgets.QLabel(self.centralwidget)
        self.student2.setGeometry(QtCore.QRect(510, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.student2.setFont(font)
        self.student2.setObjectName("student2")
        self.list_1 = QtWidgets.QListView(self.centralwidget)
        self.list_1.setGeometry(QtCore.QRect(250, 120, 211, 192))
        self.list_1.setObjectName("list_1")
        self.list_2 = QtWidgets.QListView(self.centralwidget)
        self.list_2.setGeometry(QtCore.QRect(500, 120, 211, 192))
        self.list_2.setObjectName("list_2")
        Student_Grade.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Student_Grade)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 23))
        self.menubar.setObjectName("menubar")
        Student_Grade.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Student_Grade)
        self.statusbar.setObjectName("statusbar")
        Student_Grade.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.ket_qua)
        self.semester1.clicked.connect(self.check1)
        self.semester2.clicked.connect(self.check2)



        self.retranslateUi(Student_Grade)
        QtCore.QMetaObject.connectSlotsByName(Student_Grade)

    def check1(self):
        self.semester1.setChecked(False)
    def check2(self):
        self.semester2.setChecked(False)


    def ket_qua(self):
        Name = self.name_out.text()
        Test_1 = float(self.test1_out.text())
        Test_2 = float(self.test2_out.text())
        Test_3 = float(self.test3_out.text())
        TB = (Test_1 + Test_2 + Test3) / 3
        if self.semester1.isChecked():
            a = f"{Name}, {Test_1},{Test_2},{Test3}, {TB}"
            self.list_1.setText(a)
        elif self.semester2.isChecked():
            b = f"{Name}, {Test_1},{Test_2},{Test3}, {TB}"
            self.list_2.setText(b)

    def retranslateUi(self, Student_Grade):
        _translate = QtCore.QCoreApplication.translate
        Student_Grade.setWindowTitle(_translate("Student_Grade", "MainWindow"))
        self.test1.setText(_translate("Student_Grade", "Test 1:"))
        self.test2.setText(_translate("Student_Grade", "Test 2:"))
        self.test3.setText(_translate("Student_Grade", "Test 3:"))
        self.name.setText(_translate("Student_Grade", "Name:"))
        self.semester1.setText(_translate("Student_Grade", "semester 1"))
        self.semester2.setText(_translate("Student_Grade", "semester 2"))
        self.submit.setText(_translate("Student_Grade", "Submit Grades"))
        self.student1.setText(_translate("Student_Grade", "Semester 1 -  Student List"))
        self.student2.setText(_translate("Student_Grade", "Semester 2 -  Student List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student_Grade = QtWidgets.QMainWindow()
    ui = Ui_Student_Grade()
    ui.setupUi(Student_Grade)
    Student_Grade.show()
    sys.exit(app.exec_())

