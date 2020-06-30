from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QInputDialog, QLineEdit, QDialog, QComboBox, 
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QMessageBox,
QVBoxLayout)

from math import sqrt

import sys


class Argument:

    name = ""
    charge = 0
    x = 0
    y = 0
    z = 0

    def __init__(self, name, charge, x, y, z):
        self.name = name
        self.charge = charge
        self.x = x
        self.y = y
        self.z = z

class Point:

    Ex = 0
    Ey = 0
    Ez = 0
    E = 0

    def __init__(self, x, y, z):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def getE(self):
        return (self.Ex, self.Ey, self.Ez)

    def setE(self, xE, Ey, Ez):
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez

class Application(QWidget):

    k = 1.38*pow(10,-23) #stała boltzmana
    e = 1.6*pow(10,-19)  #ładunek elementarny
    number_of_arguments = 0

    def __init__(self):
        super().__init__()
        self.title = 'ZugSpitze'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.list_of_arguments = []
        self.distances = []
        self.point = Point(0, 0, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.getNumberOfArguments()
        self.getArguments()
        self.getPoint()
        self.calculateDistance()
        self.calculateComponents()
        sys.exit(self)

    def getNumberOfArguments(self):
        self.number_of_arguments, okPressed = QInputDialog.getInt(self, "Get number of arguments", "Arguments:", 0, 0, 2147483647, 1)
        
    def getArguments(self):
        for i in range(self.number_of_arguments):
            name, okPressed = QInputDialog.getText(self, "Arguments","Name", QLineEdit.Normal, "")
            charge, okPressed = QInputDialog.getInt(self, "Arguments:", "Charge", 0, 0, 2147483647, 1)
            x, okPressed = QInputDialog.getDouble(self, "Arguments:", "x", 0, -2147483648, 2147483647, 1)
            y, okPressed = QInputDialog.getDouble(self, "Arguments:", "y", 0, -2147483648, 2147483647, 1)
            z, okPressed = QInputDialog.getDouble(self, "Arguments:", "z", 0, -2147483648, 2147483647, 1)
            if(okPressed):
                self.list_of_arguments.append(Argument(name, charge, x, y, z))
    
    def getPoint(self):
        x, okPressed = QInputDialog.getDouble(self, "Arguments:", "x", 0, -2147483648, 2147483647, 1)
        y, okPressed = QInputDialog.getDouble(self, "Arguments:", "y", 0, -2147483648, 2147483647, 1)
        z, okPressed = QInputDialog.getDouble(self, "Arguments:", "z", 0, -2147483648, 2147483647, 1)
        if(okPressed):
            self.point = Point(x, y, z)

    def calculateDistance(self):
        for i in range(len(self.list_of_arguments)):
            self.distances.append([self.point.x - self.list_of_arguments[i].x,
                                   self.point.y - self.list_of_arguments[i].y,
                                   self.point.z - self.list_of_arguments[i].z])

    def calculateComponents(self):
        for i in range(len(self.list_of_arguments)):
            self.point.Ex = self.point.Ex + (Application.k * self.list_of_arguments[i].charge) / self.distances[i][0]**2
            self.point.Ey = self.point.Ey + (Application.k * self.list_of_arguments[i].charge) / self.distances[i][1]**2
            self.point.Ez = self.point.Ez + (Application.k * self.list_of_arguments[i].charge) / self.distances[i][2]**2
        self.point.E = self.point.E + sqrt(self.point.Ex**2 + self.point.Ey**2 + self.point.Ez**2)
        QMessageBox.question(self, "Result", "Result = " + str(self.point.E), QMessageBox.Ok, QMessageBox.Ok)


application = QApplication([])
app = Application()

sys.exit(application.exec_())