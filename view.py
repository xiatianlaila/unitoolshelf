import sys
import Qt.QtWidgets as QtWidgets

app = QtWidgets.QApplication(sys.argv)
#label = QLabel("Hello World!")
label = QtWidgets.QLabel("<font color=red size=40>Hello World!</font>")
label.resize(400, 300)
label.show()
app.exec_()