"""2186400330"""
"""lÊ nGUYỄN Anh Nhật"""
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import random
import os.path
import os


class Ui_BOOK_Anhnhat(object):
    def setupUi(self, BOOK_Anhnhat):
        BOOK_Anhnhat.setObjectName("BOOK_Anhnhat")
        BOOK_Anhnhat.resize(711, 620)
        self.centralwidget = QtWidgets.QWidget(BOOK_Anhnhat)
        self.centralwidget.setObjectName("centralwidget")
        self.BOOK = QtWidgets.QLabel(self.centralwidget)
        self.BOOK.setGeometry(QtCore.QRect(130, 0, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(72)
        self.BOOK.setFont(font)
        self.BOOK.setAutoFillBackground(False)
        self.BOOK.setFrameShape(QtWidgets.QFrame.Box)
        self.BOOK.setAlignment(QtCore.Qt.AlignCenter)
        self.BOOK.setObjectName("BOOK")
        self.ma_sach = QtWidgets.QLabel(self.centralwidget)
        self.ma_sach.setGeometry(QtCore.QRect(10, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ma_sach.setFont(font)
        self.ma_sach.setObjectName("ma_sach")
        self.line_ma = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ma.setGeometry(QtCore.QRect(100, 130, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_ma.setFont(font)
        self.line_ma.setObjectName("line_ma")
        self.ten_sach = QtWidgets.QLabel(self.centralwidget)
        self.ten_sach.setGeometry(QtCore.QRect(10, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ten_sach.setFont(font)
        self.ten_sach.setObjectName("ten_sach")
        self.tac_gia = QtWidgets.QLabel(self.centralwidget)
        self.tac_gia.setGeometry(QtCore.QRect(10, 230, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tac_gia.setFont(font)
        self.tac_gia.setObjectName("tac_gia")
        self.ton_kho = QtWidgets.QLabel(self.centralwidget)
        self.ton_kho.setGeometry(QtCore.QRect(370, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ton_kho.setFont(font)
        self.ton_kho.setObjectName("ton_kho")
        self.da_ban = QtWidgets.QLabel(self.centralwidget)
        self.da_ban.setGeometry(QtCore.QRect(370, 180, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.da_ban.setFont(font)
        self.da_ban.setObjectName("da_ban")
        self.gia_ban = QtWidgets.QLabel(self.centralwidget)
        self.gia_ban.setGeometry(QtCore.QRect(370, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gia_ban.setFont(font)
        self.gia_ban.setObjectName("gia_ban")
        self.line_ten = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ten.setGeometry(QtCore.QRect(100, 180, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_ten.setFont(font)
        self.line_ten.setObjectName("line_ten")
        self.line_tac = QtWidgets.QLineEdit(self.centralwidget)
        self.line_tac.setGeometry(QtCore.QRect(100, 230, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_tac.setFont(font)
        self.line_tac.setObjectName("line_tac")
        self.line_gia = QtWidgets.QLineEdit(self.centralwidget)
        self.line_gia.setGeometry(QtCore.QRect(460, 130, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_gia.setFont(font)
        self.line_gia.setObjectName("line_gia")
        self.line_da = QtWidgets.QLineEdit(self.centralwidget)
        self.line_da.setGeometry(QtCore.QRect(460, 180, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_da.setFont(font)
        self.line_da.setObjectName("line_da")
        self.line_ton = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ton.setGeometry(QtCore.QRect(460, 230, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_ton.setFont(font)
        self.line_ton.setObjectName("line_ton")
        self.Thank_you = QtWidgets.QLabel(self.centralwidget)
        self.Thank_you.setGeometry(QtCore.QRect(250, 520, 201, 61))
        self.Thank_you.setText("")
        self.Thank_you.setPixmap(QtGui.QPixmap("../Administrator/Pictures/ảnh pyton/tải xuống (1).jpg"))
        self.Thank_you.setScaledContents(True)
        self.Thank_you.setObjectName("Thank_you")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(10, 440, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.search_name = QtWidgets.QPushButton(self.centralwidget)
        self.search_name.setGeometry(QtCore.QRect(250, 180, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_name.setFont(font)
        self.search_name.setObjectName("search_name")
        self.loc_sp = QtWidgets.QPushButton(self.centralwidget)
        self.loc_sp.setGeometry(QtCore.QRect(530, 440, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loc_sp.setFont(font)
        self.loc_sp.setObjectName("loc_sp")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(250, 440, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update.setFont(font)
        self.update.setObjectName("update")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(130, 440, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_2.setFont(font)
        self.delete_2.setObjectName("delete_2")
        self.quanly_sach = QtWidgets.QPushButton(self.centralwidget)
        self.quanly_sach.setGeometry(QtCore.QRect(390, 440, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quanly_sach.setFont(font)
        self.quanly_sach.setObjectName("quanly_sach")
        self.bieu_do = QtWidgets.QPushButton(self.centralwidget)
        self.bieu_do.setGeometry(QtCore.QRect(480, 480, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bieu_do.setFont(font)
        self.bieu_do.setObjectName("bieu_do")
        self.sort_tonkho = QtWidgets.QPushButton(self.centralwidget)
        self.sort_tonkho.setGeometry(QtCore.QRect(240, 480, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sort_tonkho.setFont(font)
        self.sort_tonkho.setObjectName("sort_tonkho")
        self.sort_daban = QtWidgets.QPushButton(self.centralwidget)
        self.sort_daban.setGeometry(QtCore.QRect(10, 480, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sort_daban.setFont(font)
        self.sort_daban.setObjectName("sort_daban")
        self.chon_nam = QtWidgets.QComboBox(self.centralwidget)
        self.chon_nam.setGeometry(QtCore.QRect(100, 260, 151, 22))
        self.chon_nam.setObjectName("chon_nam")
        self.nam = QtWidgets.QLabel(self.centralwidget)
        self.nam.setGeometry(QtCore.QRect(10, 270, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nam.setFont(font)
        self.nam.setObjectName("nam")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(30, 340, 551, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Result.setFont(font)
        self.Result.setFrameShape(QtWidgets.QFrame.Box)
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(590, 370, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.nhap_ma = QtWidgets.QLabel(self.centralwidget)
        self.nhap_ma.setGeometry(QtCore.QRect(370, 270, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nhap_ma.setFont(font)
        self.nhap_ma.setObjectName("nhap_ma")
        self.id_book = QtWidgets.QLineEdit(self.centralwidget)
        self.id_book.setGeometry(QtCore.QRect(490, 270, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_book.setFont(font)
        self.id_book.setObjectName("id_book")
        self.tim_sach = QtWidgets.QPushButton(self.centralwidget)
        self.tim_sach.setGeometry(QtCore.QRect(610, 270, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tim_sach.setFont(font)
        self.tim_sach.setObjectName("tim_sach")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 300, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        BOOK_Anhnhat.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BOOK_Anhnhat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menubar.setObjectName("menubar")
        BOOK_Anhnhat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BOOK_Anhnhat)
        self.statusbar.setObjectName("statusbar")
        BOOK_Anhnhat.setStatusBar(self.statusbar)

        self.line_ma = random.randint(100000, 999999)

        self.ok.clicked.connect(self.thongtin_sach)

        self.add.clicked.connect(self.addbook)
        self.tim_sach.clicked.connect(self.viewBook)
        self.delete_2.clicked.connect(self.delete_book)
        self.update.clicked.connect(self.Update_book)
        self.search_name.clicked.connect(self.search_nameBook)
        self.quanly_sach.clicked.connect(self.quanli_sanpham)

        self.retranslateUi(BOOK_Anhnhat)
        QtCore.QMetaObject.connectSlotsByName(BOOK_Anhnhat)
        self.addyearcombobox()
    def retranslateUi(self, BOOK_Anhnhat):
        _translate = QtCore.QCoreApplication.translate
        BOOK_Anhnhat.setWindowTitle(_translate("BOOK_Anhnhat", "MainWindow"))
        self.BOOK.setText(_translate("BOOK_Anhnhat", "BOOK"))
        self.ma_sach.setText(_translate("BOOK_Anhnhat", "Mã Sách:"))
        self.ten_sach.setText(_translate("BOOK_Anhnhat", "Tên sách:"))
        self.tac_gia.setText(_translate("BOOK_Anhnhat", "Tác Giã:"))
        self.ton_kho.setText(_translate("BOOK_Anhnhat", "Tồn kho: "))
        self.da_ban.setText(_translate("BOOK_Anhnhat", "Đã bán:"))
        self.gia_ban.setText(_translate("BOOK_Anhnhat", "Giá Bán:"))
        self.add.setText(_translate("BOOK_Anhnhat", "Add book"))
        self.search_name.setText(_translate("BOOK_Anhnhat", "search name"))
        self.loc_sp.setText(_translate("BOOK_Anhnhat", "Lọc sản phẩm "))
        self.update.setText(_translate("BOOK_Anhnhat", "Update Book"))
        self.delete_2.setText(_translate("BOOK_Anhnhat", "Delete Book"))
        self.quanly_sach.setText(_translate("BOOK_Anhnhat", "Quản Lý sách"))
        self.bieu_do.setText(_translate("BOOK_Anhnhat", "Biểu đồ doanh thu"))
        self.sort_tonkho.setText(_translate("BOOK_Anhnhat", "Sắp xếp theo tồn kho"))
        self.sort_daban.setText(_translate("BOOK_Anhnhat", "sắp xếp theo đã bán"))
        self.nam.setText(_translate("BOOK_Anhnhat", "Năm:"))
        self.ok.setText(_translate("BOOK_Anhnhat", "OK"))
        self.nhap_ma.setText(_translate("BOOK_Anhnhat", "Nhập mã sách:"))
        self.tim_sach.setText(_translate("BOOK_Anhnhat", "Tìm sách"))
        self.label.setText(_translate("BOOK_Anhnhat", "Sl bán: "))

    def addyearcombobox(self):
        Year = ['2017', '2018', '2019', '2020', '2021', '2022']
        self.chon_nam.addItems(Year)

    def loadBook(self, fn):
        data = []
        if os.path.exists(fn):
            with open(fn) as f:
                if os.stat(fn).st_size != 0:
                    data = json.load(f)
        return data

    def id_exits(self, id, data):
        for k in data:
            if str(k["Ma sach"]) == str(id):
                return k
        return None

    def name_exits(self, name, data):
        for k in data:
            if str(k["Ten sach"]) == str(name):
                return k
        return None


    def createbook(self):
        st = {}
        st["Ma sach"]=str(self.line_ma)
        st["Ten sach"] = self.line_ten.text()
        st["Gia ban"] = self.line_gia.text()
        st["Da ban"] = self.line_da.text()
        st["Ton kho"]= self.line_ton.text()
        st["Tac gia"]=self.line_tac.text()
        st["Year"]=self.chon_nam.currentText()
        return st
    def chinh_thong_tin_vesoluong(self):
        st={}
        st["Ten sach"] = self.line_ten.text()
        st["Gia ban"]=self.line_gia.text()
        st["Da ban"] = self.line_da.text()
        st["Ton kho"]=self.line_ton.text()
        return st

    def thongtin_sach(self):
        A=self.createbook()
        try:
            if float(A["Gia ban"])>0 and int(A["Da ban"])>=0 and int(A["Ton kho"])>=0:
                b=f"{A}"
                self.Result.setText(b)
            else:
                raise Exception
        except Exception:
            self.Result.setText('incorrect data')



    def addbook(self):
        fn="booknhat.json"
        data = self.loadBook(fn)

        if self.id_exits(self.line_ma,data) is not None:
            self.Result.setText("Mã đả có trong danh sách")
        else:
            add_book = self.createbook()
            data.append(add_book)
            with open(fn, "w") as book:
                json.dump(data, book)

    def viewBook(self):
        data = self.loadBook("booknhat.json")
        st = self.id_exits(self.id_book.text(), data)
        if st is None:
            self.Result.setText("Mã không có trong danh sách")

        else:
            A=f"{st}"
            self.Result.setText(A)


    def delete_book(self):
        data = self.loadBook("booknhat.json")
        k = self.id_exits(self.id_book.text(), data)
        if k is None:
            self.Result.setText("Không có cuốn sách này")
        else:
            with open("booknhat.json") as book:
                delete = json.load(book)
            delete.remove(k)
            with open("booknhat.json", "w") as nhat:
                json.dump(delete, nhat)

    def Update_book(self):
        fn = "booknhat.json"
        data = self.loadBook(fn)
        st = self.id_exits(self.id_book.text(), data)
        if st is None:
            self.Result.setText("Không có cuốn sách này")
        else:
            st_new = self.createbook()
            data.remove(st)
            data.append(st_new)
            with open(fn, "w") as book:
                json.dump(data, book)

    def quanli_sanpham(self):
        fn="booknhat.json"
        data = self.loadBook(fn)
        st = self.id_exits(self.id_book.text(), data)
        sl_daban=self.lineEdit.text()
        if st is None:
            self.Result.setText("Không có cuốn sách này")

        else:
            with open("booknhat.json") as book:
                quan_li = json.load(book)
                quan_li.remove(st)
            st["Da ban"]=str(int(st["Da ban"])+int(sl_daban))
            quan_li.append(st)
            with open("booknhat.json", "w") as nhat:
                json.dump(quan_li, nhat)

    def search_nameBook(self):
        data = self.loadBook("booknhat.json")
        st = self.name_exits(self.line_ten.text(), data)
        if st is None:
            self.Result.setText("Mã không có trong danh sách")

        else:
            A = f"{st}"
            self.Result.setText(A)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BOOK_Anhnhat = QtWidgets.QMainWindow()
    ui = Ui_BOOK_Anhnhat()
    ui.setupUi(BOOK_Anhnhat)
    BOOK_Anhnhat.show()
    sys.exit(app.exec_())


