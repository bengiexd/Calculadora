##########################################
# 
# Version: 0.1
#   Fecha: 17-julio-2013    01:00:00
#      by: Abad X 
#
##########################################

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ventana(object):
    def setupUi(self, Ventana):
        Ventana.setObjectName(_fromUtf8("Ventana"))
        Ventana.resize(347, 272)
        self.pBt_7 = QtGui.QPushButton(Ventana)
        self.pBt_7.setGeometry(QtCore.QRect(30, 60, 51, 41))
        self.pBt_7.setObjectName(_fromUtf8("pBt_7"))
        self.py_lineEdit_resultado = QtGui.QLineEdit(Ventana)
        self.py_lineEdit_resultado.setGeometry(QtCore.QRect(30, 16, 291, 31))
        self.py_lineEdit_resultado.setObjectName(_fromUtf8("py_lineEdit_resultado"))
        self.pBt_8 = QtGui.QPushButton(Ventana)
        self.pBt_8.setGeometry(QtCore.QRect(90, 60, 51, 41))
        self.pBt_8.setObjectName(_fromUtf8("pBt_8"))
        self.pBt_9 = QtGui.QPushButton(Ventana)
        self.pBt_9.setGeometry(QtCore.QRect(150, 60, 51, 41))
        self.pBt_9.setObjectName(_fromUtf8("pBt_9"))
        self.pBt_5 = QtGui.QPushButton(Ventana)
        self.pBt_5.setGeometry(QtCore.QRect(90, 110, 51, 41))
        self.pBt_5.setObjectName(_fromUtf8("pBt_5"))
        self.pBt_4 = QtGui.QPushButton(Ventana)
        self.pBt_4.setGeometry(QtCore.QRect(30, 110, 51, 41))
        self.pBt_4.setObjectName(_fromUtf8("pBt_4"))
        self.pBt_6 = QtGui.QPushButton(Ventana)
        self.pBt_6.setGeometry(QtCore.QRect(150, 110, 51, 41))
        self.pBt_6.setObjectName(_fromUtf8("pBt_6"))
        self.pBt_2 = QtGui.QPushButton(Ventana)
        self.pBt_2.setGeometry(QtCore.QRect(90, 160, 51, 41))
        self.pBt_2.setObjectName(_fromUtf8("pBt_2"))
        self.pBt_1 = QtGui.QPushButton(Ventana)
        self.pBt_1.setGeometry(QtCore.QRect(30, 160, 51, 41))
        self.pBt_1.setObjectName(_fromUtf8("pBt_1"))
        self.pBt_3 = QtGui.QPushButton(Ventana)
        self.pBt_3.setGeometry(QtCore.QRect(150, 160, 51, 41))
        self.pBt_3.setObjectName(_fromUtf8("pBt_3"))
        self.pBt_menos = QtGui.QPushButton(Ventana)
        self.pBt_menos.setGeometry(QtCore.QRect(210, 160, 51, 41))
        self.pBt_menos.setObjectName(_fromUtf8("pBt_menos"))
        self.pBt_div = QtGui.QPushButton(Ventana)
        self.pBt_div.setGeometry(QtCore.QRect(270, 160, 51, 41))
        self.pBt_div.setObjectName(_fromUtf8("pBt_div"))
        self.pBt_por = QtGui.QPushButton(Ventana)
        self.pBt_por.setGeometry(QtCore.QRect(210, 110, 51, 41))
        self.pBt_por.setObjectName(_fromUtf8("pBt_por"))
        self.pBt_porc = QtGui.QPushButton(Ventana)
        self.pBt_porc.setGeometry(QtCore.QRect(150, 210, 51, 41))
        self.pBt_porc.setObjectName(_fromUtf8("pBt_porc"))
        self.pBt_mas = QtGui.QPushButton(Ventana)
        self.pBt_mas.setGeometry(QtCore.QRect(210, 210, 51, 41))
        self.pBt_mas.setObjectName(_fromUtf8("pBt_mas"))
        self.pBt_coma = QtGui.QPushButton(Ventana)
        self.pBt_coma.setGeometry(QtCore.QRect(90, 210, 51, 41))
        self.pBt_coma.setObjectName(_fromUtf8("pBt_coma"))
        self.pBt_0 = QtGui.QPushButton(Ventana)
        self.pBt_0.setGeometry(QtCore.QRect(30, 210, 51, 41))
        self.pBt_0.setObjectName(_fromUtf8("pBt_0"))
        self.pBt_igual = QtGui.QPushButton(Ventana)
        self.pBt_igual.setGeometry(QtCore.QRect(210, 60, 111, 41))
        self.pBt_igual.setObjectName(_fromUtf8("pBt_igual"))
        self.pBt_limpiar = QtGui.QPushButton(Ventana)
        self.pBt_limpiar.setGeometry(QtCore.QRect(270, 110, 51, 41))
        self.pBt_limpiar.setObjectName(_fromUtf8("pBt_limpiar"))
        self.pBt_cuad = QtGui.QPushButton(Ventana)
        self.pBt_cuad.setGeometry(QtCore.QRect(270, 210, 51, 41))
        self.pBt_cuad.setObjectName(_fromUtf8("pBt_cuad"))

        self.retranslateUi(Ventana)

        ## eventos de los botones
        QtCore.QObject.connect(self.pBt_9, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar9)
        QtCore.QObject.connect(self.pBt_8, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar8)
        QtCore.QObject.connect(self.pBt_7, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar7)
        QtCore.QObject.connect(self.pBt_6, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar6)
        QtCore.QObject.connect(self.pBt_5, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar5)
        QtCore.QObject.connect(self.pBt_4, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar4)
        QtCore.QObject.connect(self.pBt_3, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar3)
        QtCore.QObject.connect(self.pBt_2, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar2)
        QtCore.QObject.connect(self.pBt_1, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar1)
        QtCore.QObject.connect(self.pBt_0, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregar0)                        
        QtCore.QObject.connect(self.pBt_por, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarMult)
        QtCore.QObject.connect(self.pBt_div, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarDiv)
        QtCore.QObject.connect(self.pBt_mas, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarSuma)
        QtCore.QObject.connect(self.pBt_menos, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarResta)
        QtCore.QObject.connect(self.pBt_coma, QtCore.SIGNAL(_fromUtf8("pressed()")), self.agregarComa)
        QtCore.QObject.connect(self.pBt_igual, QtCore.SIGNAL(_fromUtf8("pressed()")), self.EvaluarFuncion)
        QtCore.QObject.connect(self.pBt_limpiar, QtCore.SIGNAL(_fromUtf8("pressed()")), self.py_lineEdit_resultado.clear)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(_translate("Ventana", "Abad X Calculator V 0.1", None))
        self.pBt_7.setText(_translate("Ventana", "7", None))
        self.pBt_8.setText(_translate("Ventana", "8", None))
        self.pBt_9.setText(_translate("Ventana", "9", None))
        self.pBt_5.setText(_translate("Ventana", "5", None))
        self.pBt_4.setText(_translate("Ventana", "4", None))
        self.pBt_6.setText(_translate("Ventana", "6", None))
        self.pBt_2.setText(_translate("Ventana", "2", None))
        self.pBt_1.setText(_translate("Ventana", "1", None))
        self.pBt_3.setText(_translate("Ventana", "3", None))
        self.pBt_menos.setText(_translate("Ventana", "-", None))
        self.pBt_div.setText(_translate("Ventana", "/", None))
        self.pBt_por.setText(_translate("Ventana", "*", None))
        self.pBt_porc.setText(_translate("Ventana", "%", None))
        self.pBt_mas.setText(_translate("Ventana", "+", None))
        self.pBt_coma.setText(_translate("Ventana", ",", None))
        self.pBt_0.setText(_translate("Ventana", "0", None))
        self.pBt_igual.setText(_translate("Ventana", "=", None))
        self.pBt_limpiar.setText(_translate("Ventana", "C", None))
        self.pBt_cuad.setText(_translate("Ventana", "X2", None))

    #funciones para agregar numeros al evaluador
    def agregar9(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "9")
    def agregar8(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "8")
    def agregar7(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "7")
    def agregar6(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "6")
    def agregar5(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "5")
    def agregar4(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "4")
    def agregar3(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "3")
    def agregar2(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "2")
    def agregar1(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "1")
    def agregar0(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "0")
    def agregarMult(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "*")
    def agregarDiv(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "/")
    def agregarSuma(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "+")
    def agregarResta(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + "-")
    def agregarComa(self):
        self.py_lineEdit_resultado.setText(self.py_lineEdit_resultado.text() + ",")

    # funcion para evaluar las expresiones aritmeticas
    def EvaluarFuncion(self):
        try:
            self.py_lineEdit_resultado.setText(str(eval(str(self.py_lineEdit_resultado.text()))))
        except SyntaxError:
            self.py_lineEdit_resultado.setText("Error Sintaxis")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Ventana = QtGui.QWidget()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    Ventana.show()
    sys.exit(app.exec_())
