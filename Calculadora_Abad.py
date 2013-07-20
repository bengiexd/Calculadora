##########################################
# 
# Version: 0.1
#   Fecha: 19-julio-2013    19:22:00
#      by: Abad X 
#
##########################################

import math

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

def Operar(N1,N2,operador):
    resultado = 0
    if(operador == '-'):
        resultado = N1 - N2
    if(operador == '+'):
        resultado = N1 + N2  
    if(operador == '*'):
        resultado = N1 * N2
    if(operador == '/'):
        resultado = N1 / N2
    if(operador == '%'):
        resultado = (N1/100)* N2    

    return resultado 

class Ui_Calculator(object):
    global N1
    global N2
    global operador   
    global isN1Null
    global verificarN1
    global clean
    isN1Null= True 
    verificarN1 = True
    clean = False
    def setupUi(self, Calculator):        

        Calculator.setObjectName(_fromUtf8("Calculator"))
        Calculator.resize(309, 396)
        self.tfPantalla = QtGui.QLineEdit(Calculator)
        self.tfPantalla.setEnabled(False)
        self.tfPantalla.setGeometry(QtCore.QRect(10, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tfPantalla.setText('0')
        self.tfPantalla.setFont(font)
        self.tfPantalla.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tfPantalla.setObjectName(_fromUtf8("tfPantalla"))
        self.btnPi = QtGui.QPushButton(Calculator)
        self.btnPi.setGeometry(QtCore.QRect(10, 80, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPi.setFont(font)
        self.btnPi.setObjectName(_fromUtf8("btnPi"))
        self.btnE = QtGui.QPushButton(Calculator)
        self.btnE.setGeometry(QtCore.QRect(60, 80, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnE.setFont(font)
        self.btnE.setObjectName(_fromUtf8("btnE"))
        self.btnC = QtGui.QPushButton(Calculator)
        self.btnC.setGeometry(QtCore.QRect(110, 80, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btnC.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnC.setFont(font)
        self.btnC.setAutoFillBackground(False)
        self.btnC.setObjectName(_fromUtf8("btnC"))
        self.btnDel = QtGui.QPushButton(Calculator)
        self.btnDel.setGeometry(QtCore.QRect(160, 80, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDel.setFont(font)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.btnInv = QtGui.QPushButton(Calculator)
        self.btnInv.setGeometry(QtCore.QRect(210, 80, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnInv.setFont(font)
        self.btnInv.setObjectName(_fromUtf8("btnInv"))
        self.btnNeg = QtGui.QPushButton(Calculator)
        self.btnNeg.setGeometry(QtCore.QRect(260, 80, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnNeg.setFont(font)
        self.btnNeg.setObjectName(_fromUtf8("btnNeg"))
        self.btnCuadrado = QtGui.QPushButton(Calculator)
        self.btnCuadrado.setGeometry(QtCore.QRect(10, 130, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCuadrado.setFont(font)
        self.btnCuadrado.setObjectName(_fromUtf8("btnCuadrado"))
        self.btn7 = QtGui.QPushButton(Calculator)
        self.btn7.setGeometry(QtCore.QRect(110, 130, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.btnSqr = QtGui.QPushButton(Calculator)
        self.btnSqr.setGeometry(QtCore.QRect(60, 130, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSqr.setFont(font)
        self.btnSqr.setObjectName(_fromUtf8("btnSqr"))
        self.btnLog = QtGui.QPushButton(Calculator)
        self.btnLog.setGeometry(QtCore.QRect(60, 180, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnLog.setFont(font)
        self.btnLog.setObjectName(_fromUtf8("btnLog"))
        self.btnSin = QtGui.QPushButton(Calculator)
        self.btnSin.setGeometry(QtCore.QRect(10, 180, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSin.setFont(font)
        self.btnSin.setObjectName(_fromUtf8("btnSin"))
        self.btnDiv = QtGui.QPushButton(Calculator)
        self.btnDiv.setGeometry(QtCore.QRect(260, 130, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDiv.setFont(font)
        self.btnDiv.setObjectName(_fromUtf8("btnDiv"))
        self.btn9 = QtGui.QPushButton(Calculator)
        self.btn9.setGeometry(QtCore.QRect(210, 130, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setObjectName(_fromUtf8("btn9"))
        self.btn8 = QtGui.QPushButton(Calculator)
        self.btn8.setGeometry(QtCore.QRect(160, 130, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setObjectName(_fromUtf8("btn8"))
        self.btnMult = QtGui.QPushButton(Calculator)
        self.btnMult.setGeometry(QtCore.QRect(260, 180, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnMult.setFont(font)
        self.btnMult.setObjectName(_fromUtf8("btnMult"))
        self.btn6 = QtGui.QPushButton(Calculator)
        self.btn6.setGeometry(QtCore.QRect(210, 180, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.btn5 = QtGui.QPushButton(Calculator)
        self.btn5.setGeometry(QtCore.QRect(160, 180, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setObjectName(_fromUtf8("btn5"))
        self.btn4 = QtGui.QPushButton(Calculator)
        self.btn4.setGeometry(QtCore.QRect(110, 180, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setObjectName(_fromUtf8("btn4"))
        self.btn1 = QtGui.QPushButton(Calculator)
        self.btn1.setGeometry(QtCore.QRect(110, 230, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.btnLn = QtGui.QPushButton(Calculator)
        self.btnLn.setGeometry(QtCore.QRect(60, 230, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnLn.setFont(font)
        self.btnLn.setObjectName(_fromUtf8("btnLn"))
        self.btnCos = QtGui.QPushButton(Calculator)
        self.btnCos.setGeometry(QtCore.QRect(10, 230, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCos.setFont(font)
        self.btnCos.setObjectName(_fromUtf8("btnCos"))
        self.btn3 = QtGui.QPushButton(Calculator)
        self.btn3.setGeometry(QtCore.QRect(210, 230, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.btn2 = QtGui.QPushButton(Calculator)
        self.btn2.setGeometry(QtCore.QRect(160, 230, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btnTan = QtGui.QPushButton(Calculator)
        self.btnTan.setGeometry(QtCore.QRect(10, 280, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTan.setFont(font)
        self.btnTan.setObjectName(_fromUtf8("btnTan"))
        self.btnSuma = QtGui.QPushButton(Calculator)
        self.btnSuma.setGeometry(QtCore.QRect(260, 230, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSuma.setFont(font)
        self.btnSuma.setObjectName(_fromUtf8("btnSuma"))
        self.btnPocentaje = QtGui.QPushButton(Calculator)
        self.btnPocentaje.setGeometry(QtCore.QRect(110, 280, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPocentaje.setFont(font)
        self.btnPocentaje.setObjectName(_fromUtf8("btnPocentaje"))
        self.btnFacto = QtGui.QPushButton(Calculator)
        self.btnFacto.setGeometry(QtCore.QRect(60, 280, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnFacto.setFont(font)
        self.btnFacto.setObjectName(_fromUtf8("btnFacto"))
        self.btn0 = QtGui.QPushButton(Calculator)
        self.btn0.setGeometry(QtCore.QRect(160, 280, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setObjectName(_fromUtf8("btn0"))
        self.btnPunto = QtGui.QPushButton(Calculator)
        self.btnPunto.setGeometry(QtCore.QRect(210, 280, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPunto.setFont(font)
        self.btnPunto.setObjectName(_fromUtf8("btnPunto"))
        self.btnResta = QtGui.QPushButton(Calculator)
        self.btnResta.setGeometry(QtCore.QRect(260, 280, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnResta.setFont(font)
        self.btnResta.setObjectName(_fromUtf8("btnResta"))
        self.btnIgual = QtGui.QPushButton(Calculator)
        self.btnIgual.setGeometry(QtCore.QRect(10, 330, 291, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnIgual.setFont(font)
        self.btnIgual.setObjectName(_fromUtf8("btnIgual"))
        self.tfPantallaAux = QtGui.QLineEdit(Calculator)
        self.tfPantallaAux.setEnabled(False)
        self.tfPantallaAux.setGeometry(QtCore.QRect(10, 10, 291, 27))
        self.tfPantallaAux.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tfPantallaAux.setObjectName(_fromUtf8("tfPantallaAux"))        
        
        self.retranslateUi(Calculator)
        QtCore.QObject.connect(self.btnPi, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Pi)
        QtCore.QObject.connect(self.btnE, QtCore.SIGNAL(_fromUtf8("clicked()")), self.E)
        QtCore.QObject.connect(self.btnC, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Ce)
        QtCore.QObject.connect(self.btnDel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Del)
        QtCore.QObject.connect(self.btnInv, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Inv)
        QtCore.QObject.connect(self.btnNeg, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Neg)
        QtCore.QObject.connect(self.btnCuadrado, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Cuadrado)
        QtCore.QObject.connect(self.btnSqr, QtCore.SIGNAL(_fromUtf8("clicked()")), self.RaizCuadrada)
        QtCore.QObject.connect(self.btn7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Siete)
        QtCore.QObject.connect(self.btn8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Ocho)
        QtCore.QObject.connect(self.btn9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Nueve)
        QtCore.QObject.connect(self.btnDiv, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Div)
        QtCore.QObject.connect(self.btn4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Cuatro)
        QtCore.QObject.connect(self.btn5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Cinco)
        QtCore.QObject.connect(self.btn6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Seis)
        QtCore.QObject.connect(self.btnMult, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Multi)
        ##QtCore.QObject.connect(self.btnLog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tfPantalla.clear)
        QtCore.QObject.connect(self.btnSin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Sin)
        QtCore.QObject.connect(self.btnCos, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Cos)
        QtCore.QObject.connect(self.btnLn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Ln)
        QtCore.QObject.connect(self.btn1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Uno)
        QtCore.QObject.connect(self.btn2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Dos)
        QtCore.QObject.connect(self.btn3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tres)
        QtCore.QObject.connect(self.btnSuma, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Suma)
        QtCore.QObject.connect(self.btnTan, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tan)
        QtCore.QObject.connect(self.btnLog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Log)
        QtCore.QObject.connect(self.btnFacto, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Fact)
        QtCore.QObject.connect(self.btnPocentaje, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Porcentaje)
        QtCore.QObject.connect(self.btn0, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Cero)
        QtCore.QObject.connect(self.btnPunto, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Punto)
        QtCore.QObject.connect(self.btnResta, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Resta)
        QtCore.QObject.connect(self.btnIgual, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Resul)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(_translate("Calculator", "Abad X Calculator V-1.1", None))
        self.btnPi.setText(_translate("Calculator", "Pi", None))
        self.btnE.setText(_translate("Calculator", "e", None))
        self.btnC.setText(_translate("Calculator", "C", None))
        self.btnDel.setText(_translate("Calculator", "Del", None))
        self.btnInv.setText(_translate("Calculator", "1/x", None))
        self.btnNeg.setText(_translate("Calculator", "+/-", None))
        self.btnCuadrado.setText(_translate("Calculator", "x^2", None))
        self.btn7.setText(_translate("Calculator", "7", None))
        self.btnSqr.setText(_translate("Calculator", "sqr", None))
        self.btnLog.setText(_translate("Calculator", "log", None))
        self.btnSin.setText(_translate("Calculator", "sin", None))
        self.btnDiv.setText(_translate("Calculator", "/", None))
        self.btn9.setText(_translate("Calculator", "9", None))
        self.btn8.setText(_translate("Calculator", "8", None))
        self.btnMult.setText(_translate("Calculator", "*", None))
        self.btn6.setText(_translate("Calculator", "6", None))
        self.btn5.setText(_translate("Calculator", "5", None))
        self.btn4.setText(_translate("Calculator", "4", None))
        self.btn1.setText(_translate("Calculator", "1", None))
        self.btnLn.setText(_translate("Calculator", "ln", None))
        self.btnCos.setText(_translate("Calculator", "cos", None))
        self.btn3.setText(_translate("Calculator", "3", None))
        self.btn2.setText(_translate("Calculator", "2", None))
        self.btnTan.setText(_translate("Calculator", "tan", None))
        self.btnSuma.setText(_translate("Calculator", "+", None))
        self.btnPocentaje.setText(_translate("Calculator", "%", None))
        self.btnFacto.setText(_translate("Calculator", "x!", None))
        self.btn0.setText(_translate("Calculator", "0", None))
        self.btnPunto.setText(_translate("Calculator", ".", None))
        self.btnResta.setText(_translate("Calculator", "-", None))
        self.btnIgual.setText(_translate("Calculator", "=", None))        

    def Cero(self):  
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('0')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('0')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '0')        
            
    def Uno(self): 
        global clean
        if clean == True:
            self.tfPantalla.setText('') 
            self.tfPantalla.setText('1')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('1')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '1')    
            
    def Dos(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('2')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('2')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '2')   

    def Tres(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('3')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('3')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '3')  

    def Cuatro(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('4')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('4')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '4')     

    def Cinco(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('5')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('5')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '5')  

    def Seis(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('6')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('6')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '6')   

    def Siete(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('7')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('7')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '7')  

    def Ocho(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('8')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('8')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '8')

    def Nueve(self):
        global clean
        if clean == True:
            aux = self.tfPantalla.text() 
            self.tfPantalla.setText('9')   
            clean = False    
        else:
            aux = self.tfPantalla.text() 
            if aux == '0':
                self.tfPantalla.setText('9')
            else:    
                self.tfPantalla.setText(self.tfPantalla.text() + '9')  

    def Resta(self):
        global isN1Null
        global N1
        global N2
        global operador
        

        if isN1Null==True:
            isN1Null = False
            N1 = float(str(self.tfPantalla.text()))  
            self.tfPantalla.setText('')
        else:
            N2 = float(str(self.tfPantalla.text()))        
            self.tfPantalla.setText('')
            self.tfPantalla.setText(str(Operar(N1,N2,operador)))
            N1 = float(str(self.tfPantalla.text())) 
        operador = '-'
        global clean
        clean = True  
    
    def Suma(self):
        global isN1Null
        global N1
        global N2
        global operador
        global clean

        if isN1Null==True:
            isN1Null = False
            N1 = float(str(self.tfPantalla.text()))  
            self.tfPantalla.setText('')
        else:
            N2 = float(str(self.tfPantalla.text()))        
            self.tfPantalla.setText('')
            self.tfPantalla.setText(str(Operar(N1,N2,operador)))
            N1 = float(str(self.tfPantalla.text())) 
        operador = '+'
        clean = True

    def Multi(self):
        global isN1Null
        global N1
        global N2
        global operador
        global clean

        if isN1Null==True:
            isN1Null = False
            N1 = float(str(self.tfPantalla.text()))  
            self.tfPantalla.setText('')
        else:
            N2 = float(str(self.tfPantalla.text()))        
            self.tfPantalla.setText('')
            self.tfPantalla.setText(str(Operar(N1,N2,operador)))
            N1 = float(str(self.tfPantalla.text())) 
        operador = '*'
        clean = True
        

    def Div(self):
        global isN1Null
        global N1
        global N2
        global operador
        global clean

        if isN1Null==True:
            isN1Null = False
            N1 = float(str(self.tfPantalla.text()))  
            self.tfPantalla.setText('')
        else:
            N2 = float(str(self.tfPantalla.text()))        
            self.tfPantalla.setText('')
            self.tfPantalla.setText(str(Operar(N1,N2,operador)))
            N1 = float(str(self.tfPantalla.text())) 
        operador = '/'
        clean = True     

    def Porcentaje(self):
        global isN1Null
        global N1
        global N2
        global operador
        global clean

        if isN1Null==True:
            isN1Null = False
            N1 = float(str(self.tfPantalla.text()))  
            self.tfPantalla.setText('')
        else:
            N2 = float(str(self.tfPantalla.text()))        
            self.tfPantalla.setText('')
            self.tfPantalla.setText(str(Operar(N1,N2,operador)))
            N1 = float(str(self.tfPantalla.text())) 
        operador = '%'
        clean = True         
        
    def Resul(self):
        global N2
        global N1
        global operador
        global Operar
        global clean
        global isN1Null
        N2 = float(str(self.tfPantalla.text()))        
        self.tfPantalla.setText('')
        self.tfPantalla.setText(str(Operar(N1,N2,operador)))
        N1 = float(str(self.tfPantalla.text()))  
        clean =True
        isN1Null= True


    def Ce(self):
        global isN1Null
        global verificarN1
        global clean
        isN1Null= True 
        verificarN1 = True
        clean = False
        self.tfPantalla.setText('0')

    def Punto(self):
        txt = self.tfPantalla.text()
        if txt.count('.') ==0:
            self.tfPantalla.setText(self.tfPantalla.text() + '.')  

    def Del(self):
        txt = self.tfPantalla.text()
        if len(txt) ==1:
            self.tfPantalla.setText('0')
        else:
            self.tfPantalla.setText(txt[0:len(txt) -1])    

    def Pi(self):
        global clean
        clean = True
        self.tfPantalla.setText(str(math.pi)) 

    def E(self):
        global clean
        clean = True
        self.tfPantalla.setText(str(math.e))

    def Inv(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(1/num)) 

    def Neg (self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(-1*num))     

    def Cuadrado(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.pow(num,2)))  

    def RaizCuadrada(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.sqrt(num)))     
    
    def Log(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.log(num,10))) 

    def Ln(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.log(num)))     

    def Sin(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.sin(math.radians(num))))            

    def Cos(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.cos(math.radians(num))))        

    def Tan(self):
        global clean
        clean = True
        num = float(self.tfPantalla.text())
        self.tfPantalla.setText(str(math.tan(math.radians(num))))  

    def Fact(self):
        global clean
        clean = True
        num = int(float(self.tfPantalla.text()))
        self.tfPantalla.setText(str(math.factorial(num)))                                                
         

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Calculator = QtGui.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
