try:
	from Pyside6 import Qtcore, Qtgui, Qtwidget
	from shiboken6 import wrapinstance
except :
	from Pyside2 import Qtcore, Qtgui, Qtwidget
	from shiboken2 import wrapinstance

import maya.OpenMayaUI as omui

class ObjectCreatorDialog(Qtwidget.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		
		self.resize(300, 300)
		self.setWindowTitle('Object Creator')

		self.main_layout = Qtwidget.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.object_listWidget = Qtwidget.QlistWidger()
		self.main_layout.addWidget(self.object_listWidget)

		self.name_layout = Qtwidget.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)
		self.name_label = Qtwidget.Qlabel('Name:')
		self.name_lineEdit = Qtwidget.QlineEdit()
		self.main_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = Qtwidget.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = Qtwidget.QPushButton('Create')
		self.cancle_button = Qtwidget.QPushButton('Cancle')
		self.button_layout.aStetch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancle_button)

	def run():
		global ui
		try:
			ui.close()
		except:
			pass

		ptr = wrapinstance(int(omui.MQtUtil.mainWindow()), Qtwidget.Qwidget)
		ui = ObjectCreatorDialog(parent=ptr)
		ui.show()