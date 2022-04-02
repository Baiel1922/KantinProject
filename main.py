from model.model import *
from PyQt5.QtCore import QSize, Qt, QTranslator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableView,\
    QGridLayout, QTableWidget, QTableWidgetItem, QMessageBox, QMainWindow, \
    QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 711))
        self.tabWidget.setMaximumSize(QtCore.QSize(1300, 1000))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")







        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.label = QtWidgets.QLabel(self.homeTab)
        self.label.setGeometry(QtCore.QRect(320, 250, 250, 300))
        self.BtnEn = QtWidgets.QPushButton(self.homeTab)
        self.BtnEn.setGeometry(QtCore.QRect(660, 10, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.BtnEn.setFont(font)
        self.BtnEn.setStyleSheet("font-family: \'Montserrat\';")
        self.BtnEn.setObjectName("BtnEn")
        self.BtnEn.clicked.connect(self.change_lan)
        self.BtnCh = QtWidgets.QPushButton(self.homeTab)
        self.BtnCh.setGeometry(QtCore.QRect(560, 10, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.BtnCh.setFont(font)
        self.BtnCh.setStyleSheet("font-family: \'Montserrat\';")
        self.BtnCh.setObjectName("BtnEn")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1519540999.2 1.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.homeTab)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 951, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: \'Montserrat\';\n"
        "letter-spacing: 0.065em;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.homeTab, "")







        font2 = QtGui.QFont()
        font.setFamily("Montserrat")
        font2.setPointSize(10)
        self.showTab = QtWidgets.QWidget()
        self.showTab.setObjectName("showTab")
        grid_layout = QGridLayout()
        self.showTab.setLayout(grid_layout)

        self.table = QtWidgets.QTableWidget()
        # self.table.setGeometry(QtCore.QRect(50, 59, 731, 471))
        self.table.setMaximumSize(QtCore.QSize(750, 500))
        self.table.setColumnCount(3)  # Устанавливаем три колонки
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.table.setFont(font)

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(["barcode", "name of product", "price"])
        json_products = self.get_all()
        row = len(json_products)
        self.table.setRowCount(row)  # установливаем строки в таблице

        # Устанавливаем всплывающие подсказки на заголовки
        self.table.horizontalHeaderItem(0).setToolTip("barcode")
        self.table.horizontalHeaderItem(1).setToolTip("name of product")
        self.table.horizontalHeaderItem(2).setToolTip("price")

        # Устанавливаем выравнивание на заголовки
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        count_column = 0
        # заполняем  строки
        for i in json_products:
            self.table.setItem(count_column, 0, QTableWidgetItem(str(i["barcode"])))
            self.table.setItem(count_column, 1, QTableWidgetItem(str(i["name"])))
            self.table.setItem(count_column, 2, QTableWidgetItem(str(i["price"])))
            count_column += 1
        # делаем ресайз колонок по содержимому
        self.table.setColumnWidth(0, 220)
        self.table.setColumnWidth(1, 420)
        self.table.setColumnWidth(2, 100)
        grid_layout.addWidget(self.table, 0, 0)
        # self.table.setGeometry(QtCore.QRect(0, 0, 450, 300))
        self.deleteBarcode = QtWidgets.QLineEdit(self.showTab)
        self.deleteBarcode.setGeometry(QtCore.QRect(480, 10, 150, 50))
        self.deleteBarcode.setText("")
        self.deleteBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.deleteBarcode.setObjectName("deleteBarcode")
        self.deleteButton = QtWidgets.QPushButton(self.showTab)
        self.deleteButton.setGeometry(QtCore.QRect(660, 10, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("font-family: \'Montserrat\';")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.delete_product)
        self.deleteBarcode.returnPressed.connect(self.deleteButton.click)

        # self.showButton = QtWidgets.QPushButton(self.showTab)
        # self.showButton.setGeometry(QtCore.QRect(200, 10, 150, 50))
        # font = QtGui.QFont()
        # font.setFamily("Montserrat")
        # font.setPointSize(15)
        # self.showButton.setFont(font)
        # self.showButton.setStyleSheet("font-family: \'Montserrat\';")
        # self.showButton.setObjectName("showButton")
        # self.showButton.clicked.connect(self.get_all)
        self.tabWidget.addTab(self.showTab, "")









        self.addTab = QtWidgets.QWidget()
        self.addTab.setObjectName("addTab")
        self.add_tableWidget = QtWidgets.QTableWidget(self.addTab)
        self.add_tableWidget.setGeometry(QtCore.QRect(50, 59, 731, 471))
        self.add_tableWidget.setMaximumSize(QtCore.QSize(1000, 620))
        self.add_tableWidget.setObjectName("add_tableWidget")
        self.add_tableWidget.setColumnCount(3)
        self.add_tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.add_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.add_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.add_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.add_tableWidget.setHorizontalHeaderItem(2, item)
        self.add_tableWidget.horizontalHeader().setDefaultSectionSize(305)
        self.add_tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.add_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.add_tableWidget.setColumnWidth(0, 270)
        self.add_tableWidget.setColumnWidth(1, 220)
        self.add_tableWidget.setColumnWidth(2, 220)
        self.addspinforRow = QtWidgets.QSpinBox(self.addTab)
        self.addspinforRow.setGeometry(QtCore.QRect(800, 120, 81, 61))
        self.addspinforRow.setMaximumSize(QtCore.QSize(81, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.addspinforRow.setFont(font)
        self.addspinforRow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addspinforRow.setWrapping(False)
        self.addspinforRow.setAlignment(QtCore.Qt.AlignCenter)
        self.addspinforRow.setMinimum(1)
        self.addspinforRow.setMaximum(200)
        self.addspinforRow.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.addspinforRow.setObjectName("addspinforRow")
        self.addButton = QtWidgets.QPushButton(self.addTab)
        self.addButton.setGeometry(QtCore.QRect(350, 540, 150, 40))
        self.addButton.setMaximumSize(QtCore.QSize(275, 81))
        self.addButton.setStyleSheet("")
        self.addButton.setObjectName("addButton")
        # self.add_otmena = QtWidgets.QPushButton(self.addTab)
        # self.add_otmena.setGeometry(QtCore.QRect(710, 640, 275, 81))
        # self.add_otmena.setMaximumSize(QtCore.QSize(275, 81))
        # self.add_otmena.setStyleSheet("")
        # self.add_otmena.setObjectName("add_otmena")
        self.add_label = QtWidgets.QLabel(self.addTab)
        self.add_label.setGeometry(QtCore.QRect(300, 10, 350, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.add_label.setFont(font)
        self.add_label.setStyleSheet("font-family: \'Montserrat\';")
        self.add_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_label.setObjectName("add_label")
        self.tabWidget.addTab(self.addTab, "")
        self.addButton.clicked.connect(self.add_product)






        self.orderTab = QtWidgets.QWidget()
        self.orderTab.setObjectName("orderTab")
        self.order_tableWidget = QtWidgets.QTableWidget(self.orderTab)
        self.order_tableWidget.setGeometry(QtCore.QRect(10, 20, 620, 510))
        self.order_tableWidget.setMaximumSize(QtCore.QSize(1000, 710))
        self.order_tableWidget.setRowCount(100)
        self.order_tableWidget.setObjectName("order_tableWidget")
        self.order_tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.order_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.order_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.order_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.order_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.order_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.order_tableWidget.setHorizontalHeaderItem(2, item)
        self.order_tableWidget.horizontalHeader().setDefaultSectionSize(188)
        self.order_tableWidget.horizontalHeader().setHighlightSections(True)
        self.order_tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.order_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.order_tableWidget.setColumnWidth(0, 180)
        self.order_tableWidget.setColumnWidth(1, 270)
        self.order_tableWidget.setColumnWidth(2, 100)
        self.order_barcode = QtWidgets.QLineEdit(self.orderTab)
        self.order_barcode.setGeometry(QtCore.QRect(670, 20, 200, 71))
        self.order_barcode.setText("")
        self.order_barcode.setAlignment(QtCore.Qt.AlignCenter)
        self.order_barcode.setObjectName("order_barcode")
        self.price_of_product = QtWidgets.QLabel(self.orderTab)
        self.price_of_product.setGeometry(QtCore.QRect(670, 430, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.price_of_product.setFont(font)
        self.price_of_product.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.price_of_product.setAlignment(QtCore.Qt.AlignCenter)
        self.price_of_product.setObjectName("price_of_product")
        self.submitButton = QtWidgets.QPushButton(self.orderTab)
        self.submitButton.setGeometry(QtCore.QRect(670, 110, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.cancelButton = QtWidgets.QPushButton(self.orderTab)
        self.cancelButton.setGeometry(QtCore.QRect(670, 500, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(self.cancel_order)
        self.payButton = QtWidgets.QPushButton(self.orderTab)
        self.payButton.setGeometry(QtCore.QRect(670, 300, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.payButton.setFont(font)
        self.payButton.setObjectName("payButton")
        self.id_student = QtWidgets.QLineEdit(self.orderTab)
        self.id_student.setGeometry(QtCore.QRect(670, 210, 200, 71))
        self.id_student.setText("")
        self.id_student.setAlignment(QtCore.Qt.AlignCenter)
        self.id_student.setObjectName("id_student")
        self.tabWidget.addTab(self.orderTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.submitButton.clicked.connect(self.start_order)
        # self.submitButton.setAutoDefault(True)  # click on <Enter>
        self.order_barcode.returnPressed.connect(self.submitButton.click)
        self.addspinforRow.valueChanged.connect(self.change)
        self.payButton.clicked.connect(self.start_payment)
        self.id_student.returnPressed.connect(self.payButton.click)

        self.c_column = 0
        self.count_money = 0
        # self.product = []
    def start_payment(self):
        rows = self.order_tableWidget.rowCount()
        student = Students()
        id_student = self.id_student.text()
        price = self.price_of_product.text()
        answer = student.substract_cash(id_student, price)
        if answer == "Not enough money!":
            QMessageBox.warning(self.orderTab, "Error", "Not enough money!")
        elif answer == "Success!":
            QMessageBox.about(self.showTab, "Success", "Success!")
            for i in range(rows):
                self.order_tableWidget.setItem(i, 0, QTableWidgetItem(""))
                self.order_tableWidget.setItem(i, 1, QTableWidgetItem(""))
                self.order_tableWidget.setItem(i, 2, QTableWidgetItem(""))
                self.price_of_product.setText("")

        elif answer == "Something went wrong!":
            QMessageBox.warning(self.orderTab, "Error", "Something went wrong!")
        elif answer == "Student's id not found!":
            QMessageBox.warning(self.orderTab, "Error", "Student's id not found!")

        self.id_student.setText("")

        self.c_column = 0
        self.count_money = 0
        # self.price_of_product.setText("")


    def start_order(self):
        barcode = self.order_barcode.text()
        product = self.get_product(barcode)
        print(product)

        try:
            self.order_tableWidget.setItem(self.c_column, 0, QTableWidgetItem(str(product["barcode"])))
            self.order_tableWidget.setItem(self.c_column, 1, QTableWidgetItem(product["name"]))
            self.order_tableWidget.setItem(self.c_column, 2, QTableWidgetItem(str(product["price"])))
            self.count_money += int(product["price"])
            self.c_column += 1
            self.price_of_product.setText(str(self.count_money))
            self.order_barcode.setText("")
        except KeyError:
            QMessageBox.warning(self.orderTab, "Error!", "The product does not exists!")
            self.order_barcode.setText("")
        except TypeError:
            QMessageBox.warning(self.orderTab, "Error!", "Enter the product's barcode!")
            self.order_barcode.setText("")



    def get_product(self, barcode):
        product_obj = Products()
        prod = product_obj.get_product(barcode)
        return prod


    def get_all(self):
        products = Products()
        json_products = products.get_all_products()
        return json_products


    def update_data(self):
        products = Products()
        json_products = products.get_all_products()
        count = self.table.rowCount()
        for i in range(count):
            self.table.removeRow(i)
        self.table.removeRow(0)
        row = len(json_products)
        self.table.setRowCount(row)
        count_column = 0
        # заполняем  строки
        for i in json_products:
            self.table.setItem(count_column, 0, QTableWidgetItem(str(i["barcode"])))
            self.table.setItem(count_column, 1, QTableWidgetItem(str(i["name"])))
            self.table.setItem(count_column, 2, QTableWidgetItem(str(i["price"])))
            count_column += 1

        # self.table.show()# Добавляем таблицу в сетку


    def delete_product(self):
        delete_barcode = self.deleteBarcode.text()
        products = Products()
        responce = products.delete_product(delete_barcode)
        self.deleteBarcode.setText("")
        print(responce)
        if responce:
            QMessageBox.about(self.showTab, "Success", "Product deleted successfully!")
            self.update_data()
        else:
            QMessageBox.warning(self.showTab, "Error", "Product does not exists")



    def add_product(self):
        rows = self.add_tableWidget.rowCount()
        cols = self.add_tableWidget.columnCount()
        data = []
        count = 0
        added = 0
        db = Products()
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.add_tableWidget.item(row, col).text())
                except:
                    tmp.append("")
            # data.append(tmp)
            # try:
            answer = db.add_product(tmp[2], tmp[0], tmp[1])
            count += 1
            if answer:
                added += 1
            else:
                QMessageBox.warning(self.addTab, "Error!", f'Product in {row + 1} row already exists!')
        if count == rows and count != 0 and added > 0:
            QMessageBox.about(self.addTab, "Success!", "Products were added successfully!")
            # else:
            #     QMessageBox.about(self.addTab, "Success!", "Other products were added successfully!")

            # except:
            #     if added == 0:
            #         QMessageBox.warning(self.addTab, "Error!", f'Nothing was added!')

        for i in range(rows):
            for i in range(2):
                try:
                    self.add_tableWidget.removeRow(i)
                except:
                    pass
        self.add_tableWidget.removeRow(0)
        self.update_data()

        # for i in data:
        #     print(i)
        #     db = Products()
            # print(data)
            # answer = db.add_product(i[2], i[0], i[1])



    def cancel_order(self):
        try:
            index_row = []
            for i in self.order_tableWidget.selectedIndexes():
                index_row.append(i.row())
            # удаляем лишнее, поскольку индекс каждой строки записывается столько раз, сколько столбцов
            index_row = list(set(index_row))
            for item in index_row:
                canceled_money = self.order_tableWidget.item(item, 2).text()
                self.order_tableWidget.setItem(item, 0, QTableWidgetItem(""))
                self.order_tableWidget.setItem(item, 1, QTableWidgetItem(""))
                self.order_tableWidget.setItem(item, 2, QTableWidgetItem(""))
                print(canceled_money)
                current_money = self.price_of_product.text()
                new_money = int(current_money) - int(canceled_money)
                self.count_money = new_money
                self.price_of_product.setText(str(new_money))
        except:
            QMessageBox.warning(self.addTab, "Error!", f'Rows are already clear!')

    def change_lan(self):
        self.txt1 = "bbbbbbbbbbbbbbbbb"

    def change(self):
        self.add_tableWidget.setRowCount(int(self.addspinforRow.text()))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ala-Too"))
        self.txt1 = "AAAAAAAAAAA"
        self.label_2.setText(_translate("MainWindow", self.txt1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("MainWindow", "Home Page"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.BtnEn.setText(_translate("MainWindow", "En"))
        self.BtnCh.setText(_translate("MainWindow", "Ch"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        # self.showButton.setText(_translate("MainWindow", "Show"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showTab), _translate("MainWindow", "Show Page"))
        item = self.add_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.add_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.add_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.add_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Barcode"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        # self.add_otmena.setText(_translate("MainWindow", "Cancel"))
        self.add_label.setText(_translate("MainWindow", "Add products"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addTab), _translate("MainWindow", "Add Product"))
        item = self.order_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.order_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.order_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.order_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Barcode"))
        item = self.order_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.order_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.price_of_product.setText(_translate("MainWindow", "0"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.payButton.setText(_translate("MainWindow", "Pay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orderTab), _translate("MainWindow", "Order "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# class MyWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MyWindow, self).__init__(parent)
#         self.setupUi(self)
#
#         #  Переводчик
#         self.trans = QTranslator()
#
#         # Подключение к функции слота
#         self.BtnEn.clicked.connect(self._trigger_english)
#         self.BtnCh.clicked.connect(self._trigger_zh_cn)
#
#     def _trigger_english(self):
#         print("[MainWindow] Change to English")
#         self.trans.load("en")
#         _app = QApplication.instance()  # получить экземпляр приложения
#
#         _app.installTranslator(self.trans)
#         # Перевести интерфейс
#         self.retranslateUi(self)
#         pass
#
#
#     def _trigger_zh_cn(self):
#         print("[MainWindow] Change to zh_CN")
#         self.trans.load("zh_CN")
#         _app = QApplication.instance()
#         _app.installTranslator(self.trans)
#         self.retranslateUi(self)
#         pass
#
#
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     mainWindow = MyWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
