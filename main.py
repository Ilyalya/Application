from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Application for Arduino")
ui.show()
app.exec()