from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import random
import json as js

class Name1Error(Exception):
    def __str__(self):
        return 'No Number'
class PhoneError(Exception):
    def __str__(self):
        return 'No anphabet'
class Phone1Error(Exception):
    def __str__(self):
        return 'Only 13 number'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 70, 431, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.name.setObjectName("name")
        self.phone_num = QtWidgets.QLabel(self.frame)
        self.phone_num.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.phone_num.setObjectName("phone_num")
        self.name_1 = QtWidgets.QLineEdit(self.frame)
        self.name_1.setGeometry(QtCore.QRect(130, 90, 191, 31))
        self.name_1.setObjectName("name_1")
        self.phone_num_1 = QtWidgets.QLineEdit(self.frame)
        self.phone_num_1.setGeometry(QtCore.QRect(130, 150, 191, 31))
        self.phone_num_1.setObjectName("phone_num_1")
        self.email = QtWidgets.QLabel(self.frame)
        self.email.setGeometry(QtCore.QRect(10, 210, 91, 31))
        self.email.setObjectName("email")
        self.email_1 = QtWidgets.QLineEdit(self.frame)
        self.email_1.setGeometry(QtCore.QRect(130, 210, 191, 31))
        self.email_1.setObjectName("email_1")
        self.information_tex = QtWidgets.QLabel(self.frame)
        self.information_tex.setGeometry(QtCore.QRect(70, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.information_tex.setFont(font)
        self.information_tex.setAlignment(QtCore.Qt.AlignCenter)
        self.information_tex.setObjectName("information_tex")

        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(10, 280, 55, 16))
        self.id.setObjectName("id")
        self.id_1 = QtWidgets.QLineEdit(self.frame)
        self.id_1.setGeometry(QtCore.QRect(130, 270, 191, 31))
        self.id_1.setObjectName("id_1")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(330, 270, 41, 31))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/user/OneDrive/Máy tính/search_icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(510, 70, 391, 241))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.typeroom_tex = QtWidgets.QLabel(self.frame_2)
        self.typeroom_tex.setGeometry(QtCore.QRect(120, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.typeroom_tex.setFont(font)
        self.typeroom_tex.setAlignment(QtCore.Qt.AlignCenter)
        self.typeroom_tex.setObjectName("typeroom_tex")
        self.joint_btn = QtWidgets.QRadioButton(self.frame_2)
        self.joint_btn.setGeometry(QtCore.QRect(70, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.joint_btn.setFont(font)
        self.joint_btn.setObjectName("joint_btn")
        self.deluxe_btn = QtWidgets.QRadioButton(self.frame_2)
        self.deluxe_btn.setGeometry(QtCore.QRect(230, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deluxe_btn.setFont(font)
        self.deluxe_btn.setObjectName("deluxe_btn")
        self.single_btn = QtWidgets.QRadioButton(self.frame_2)
        self.single_btn.setGeometry(QtCore.QRect(70, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_btn.setFont(font)
        self.single_btn.setObjectName("single_btn")
        self.double_btn = QtWidgets.QRadioButton(self.frame_2)
        self.double_btn.setGeometry(QtCore.QRect(230, 100, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.double_btn.setFont(font)
        self.double_btn.setObjectName("double_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Oxygen")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(50, 470, 101, 41))
        self.add_btn.setObjectName("add_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(200, 470, 101, 41))
        self.update_btn.setObjectName("update_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(360, 470, 101, 41))
        self.delete_btn.setObjectName("delete_btn")
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(510, 470, 111, 41))
        self.filter_btn.setObjectName("filter_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(810, 470, 101, 41))
        self.clear_btn.setObjectName("clear_btn")
        self.report_btn = QtWidgets.QPushButton(self.centralwidget)
        self.report_btn.setGeometry(QtCore.QRect(670, 470, 91, 41))
        self.report_btn.setObjectName("report_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.add_btn.clicked.connect(self.add)
        self.idinput = random.randint(100000, 999999)
        self.pushButton.clicked.connect(self.search)
        self.update_btn.clicked.connect(self.update)
        self.delete_btn.clicked.connect(self.delete)
        self.clear_btn.clicked.connect(self.clear)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.phone_num.setText(_translate("MainWindow", "Phone Number:"))
        self.email.setText(_translate("MainWindow", "Email:"))
        self.information_tex.setText(_translate("MainWindow", "Information"))
        self.id.setText(_translate("MainWindow", "ID:"))
        self.typeroom_tex.setText(_translate("MainWindow", "Type of room"))
        self.joint_btn.setText(_translate("MainWindow", "Joint"))
        self.deluxe_btn.setText(_translate("MainWindow", "Deluxe"))
        self.single_btn.setText(_translate("MainWindow", "Single"))
        self.double_btn.setText(_translate("MainWindow", "Double"))
        self.label_3.setText(_translate("MainWindow", "HOTEL CHECKIN"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.filter_btn.setText(_translate("MainWindow", "Filter"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.report_btn.setText(_translate("MainWindow", "Report"))

    def add(self):
        try:
            name = self.name_1.text()
            phone_num = self.phone_num_1.text()
            email = self.email_1.text()
            id = str(self.idinput)
            single = self.single_btn.text()
            double = self.double_btn.text()
            joint = self.joint_btn.text()
            deluxe = self.deluxe_btn.text()
            if not name.isalpha():
                raise Name1Error()
            if not phone_num.isnumeric():
                raise PhoneError()
            if len(phone_num) >= 13:
                raise Phone1Error()

            with open('HotelList.json') as f:
                hotel_list = js.load(f)
            if self.single_btn.isChecked():
                d = {"id": id, "name": name, "phone_num": phone_num, "email": email,  "type": single}
            elif self.deluxe_btn.isChecked():
                d = {"id": id, "name": name, "phone_num": phone_num, "email": email,  "type": deluxe}
            elif self.double_btn.isChecked():
                d = {"id": id, "name": name, "phone_num": phone_num, "email": email,  "type": double}
            elif self.joint_btn.isChecked():
                d = {"id": id, "name": name, "phone_num": phone_num, "email": email,  "type": joint}
            hotel_list.append(d)
            with open('HotelList.json', 'w') as f1:
                js.dump(hotel_list, f1)
            self.mess = QMessageBox()
            QMessageBox.information(self.mess, 'Successful', 'Confirm Add')
            self.mess.close()
        except Name1Error as t:
            QMessageBox.information(QMessageBox(), 'Error', f'{t}')
        except PhoneError as t:
            QMessageBox.information(QMessageBox(), 'Error', f'{t}')
        except Phone1Error as t:
            QMessageBox.information(QMessageBox(), 'Error', f'{t}')


    def search(self):
        id = self.id_1.text()
        with open('HotelList.json', 'r') as f:
            hotel_list = js.load(f)
        for i in hotel_list:
            if i['id']==id:
                self.name_1.setText(i['name'])
                self.phone_num_1.setText((i['phone_num']))
                self.email_1.setText((i['email']))
                if i['type'] == 'Single':
                    self.single_btn.setChecked(True)
                if i['type'] == 'Double':
                    self.double_btn.setChecked(True)
                if i['type'] == 'Joint':
                    self.joint_btn.setChecked(True)
                if i['type'] == 'Deluxe':
                    self.deluxe_btn.setChecked(True)


    def update(self):
            name = self.name_1.text()
            phone_num = self.phone_num_1.text()
            email = self.email_1.text()
            id = self.id_1.text()
            with open('HotelList.json') as f:
                hotel_list = js.load(f)
                for i in hotel_list:
                    if i['id'] == id:
                        i['name'] == name
                        i["email"] == email
                        i["phone_num"] == phone_num
                        if self.single_btn.isChecked():
                            i['type'] = 'Single'
                        if self.double_btn.isChecked():
                            i['type'] = 'Double'
                        if self.joint_btn.isChecked():
                            i['type'] = 'Joint'
                        if self.deluxe_btn.isChecked():
                            i['type'] = 'Deluxe'
            with open('HotelList.json', 'w') as s:
                js.dump(hotel_list, s)
            self.mess=QMessageBox()
            QMessageBox.information(self.mess, 'Successful', 'Update success')
            self.mess.close()



    def delete(self):
        id = self.id_1.text()
        with open('HotelList.json') as f:
            hotel_list = js.load(f)
            for i in hotel_list:
                if i["id"]==id:
                    hotel_list.remove(i)
        with open('HotelList.json', 'w') as s:
            js.dump(hotel_list, s)
        self.mess = QMessageBox()
        QMessageBox.information(self.mess, 'Successful', 'Delete success')
        self.mess.close()

    def clear(self):
        self.name_1.clear()
        self.phone_num_1.clear()
        self.email_1.clear()
        self.id_1.clear()
        self.single_btn.setChecked(True)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())