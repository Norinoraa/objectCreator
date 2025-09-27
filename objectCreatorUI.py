try:
	from PySide6 import Qtcore, Qtgui, Qtwidget
	from shiboken6 import wrapinstance
except :
	from PySide2 import Qtcore, Qtgui, Qtwidget
	from shiboken2 import wrapinstance

import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__flie__), 'icons'))

class ObjectCreatorDialog(Qtwidget.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		
		self.resize(300, 300)
		self.setWindowTitle('Object Creator')

		self.main_layout = Qtwidget.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.object_listWidget = Qtwidget.QlistWidget()
		self.object_listWidget.setIconSize(Qtcore.QSize(50,50))
		self.object_listWidget.setSpacing(5)
		self.object_listWidget.setViewMode(Qtwidget.QListView.IconMode)
		self.object_listWidget.setMovement(Qtwidget.QListView.Static)
		self.object_listWidget.setResizeMode(Qtwidget.QListView.Adjust)

		self.main_layout.addWidget(self.object_listWidget)

		self.name_layout = Qtwidget.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)
		self.name_label = Qtwidget.Qlabel('Name:')
		self.name_lineEdit = Qtwidget.QlineEdit()
		self.name_lineEdit.setStyleSheet(
			'''
				QlineEdit{
					border-radius: 5px;
					background-color: white;
					color: navy;
					font-size: 24px;
					font-family: Arial;
					}
			'''
		)

		self.main_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = Qtwidget.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = Qtwidget.QPushButton('Create')
		self.create_button.setStyleSheet(
			'''
				QpushButton {
					background-color: red
				}
			'''
		)
		self.cancle_button = Qtwidget.QPushButton('Cancle')
		self.button_layout.aStetch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancle_button)

	def initIconWidget(self):
		objs = ['cube', 'cone', 'sphere', 'tortus']
		for obj in objs:
			item = Qtwidget.QlistWidgetItem(obj)
			item.setIcon(Qtgui.QIcon(os.path.join(ICON_PATH, f'{obj}.png')))
			self.object_listWidget.addItem(item)

	def run():
		global ui
		try:
			ui.close()
		except:
			pass

		ptr = wrapinstance(int(omui.MQtUtil.mainWindow()), Qtwidget.Qwidget)
		ui = ObjectCreatorDialog(parent=ptr)
		ui.show()