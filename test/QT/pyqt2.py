import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연동
form_class = uic.loadUiType("qtTest1.ui")[0]

class MyApp(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn1.clicked.connect(self.btn1_clicked)
		self.btn2.clicked.connect(self.btn2_clicked)

	def btn1_clicked(self):
		print("on button was clicked")

	def btn2_clicked(self):
		print("off button was clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mywindow = MyApp()
	mywindow.show()
	sys.exit(app.exec_())
