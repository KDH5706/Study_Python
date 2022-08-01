import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("Test2.ui")[0]

class MyApp(QMainWindow, from_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.btn1.clicked.connect(self.btnCallBack)
		self.btn2.clicked.connect(self.btn2CallBack)

	def btnCallBack(self):
		print("button1 ON")
		self.text.clear()
		self.text.append("SWITCH ON")

	def btn2CallBack(self):
		print("button2 ON")
		self.text.clear()
		self.text.append("SWITCH OFF")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = MyApp()
	myWindow.show()
	sys.exit(app.exec())
