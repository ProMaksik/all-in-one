from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QApplication)

app = QApplication([])

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel("")
        self.inpt = QLabel("")
        self.token = ""
        self.inpttext = ""
        self.scobka = False
        self.setWindowTitle('Калькулятор')

        #1
        self.btnsc = QPushButton("()")
        self.btnsc.clicked.connect(self.add_scoba)
        self.btnCE = QPushButton("CE")
        self.btnCE.clicked.connect(lambda: self.inpt.setText(""))
        self.btnC = QPushButton("C")
        self.btnC.clicked.connect(self.noll)
        self.btndel = QPushButton("⌫")
        self.btndel.clicked.connect(lambda : self.inpt.setText(self.inpt.text()[:-1]))
        #2
        self.btndiv = QPushButton("¹/ₓ")
        self.btnsquare = QPushButton("x²")
        self.btnsquare.clicked.connect(self.sqr)
        self.btncb = QPushButton("x³")
        self.btncb.clicked.connect(self.cb)
        self.btndev = btn_func("/")
        #3
        self.btn7 = btn_nums("7")
        self.btn8 = btn_nums("8")
        self.btn9 = btn_nums("9")
        self.btnumn = btn_func("*")
        #4
        self.btn4 = btn_nums("4")
        self.btn5 = btn_nums("5")
        self.btn6 = btn_nums("6")
        self.btnmin = btn_func("-")
        #5
        self.btn1 = btn_nums("1")
        self.btn2 = btn_nums("2")
        self.btn3 = btn_nums("3")
        self.btnpl = btn_func("+")
        #6
        self.btnpm = QPushButton("+/-")
        self.btnpm.clicked.connect(lambda: self.inpt.setText(str(int(self.inpt.text())*-1)))
        self.btn0 = btn_nums("0")
        self.btnstr = btn_func(".")
        self.btneq = QPushButton("=")
        self.btneq.clicked.connect(self.eq)

        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        self.h8 = QHBoxLayout()
        self.v1 = QVBoxLayout()

        self.h1.addWidget(self.lbl)
        self.h2.addWidget(self.inpt)

        self.h3.addWidget(self.btnsc)
        self.h3.addWidget(self.btnC)
        self.h3.addWidget(self.btnCE)
        self.h3.addWidget(self.btndel)

        self.h4.addWidget(self.btndiv)
        self.h4.addWidget(self.btnsquare)
        self.h4.addWidget(self.btncb)
        self.h4.addWidget(self.btndev)

        self.h5.addWidget(self.btn7)
        self.h5.addWidget(self.btn8)
        self.h5.addWidget(self.btn9)
        self.h5.addWidget(self.btnumn)

        self.h6.addWidget(self.btn4)
        self.h6.addWidget(self.btn5)
        self.h6.addWidget(self.btn6)
        self.h6.addWidget(self.btnmin)

        self.h7.addWidget(self.btn1)
        self.h7.addWidget(self.btn2)
        self.h7.addWidget(self.btn3)
        self.h7.addWidget(self.btnpl)

        self.h8.addWidget(self.btnpm)
        self.h8.addWidget(self.btn0)
        self.h8.addWidget(self.btnstr)
        self.h8.addWidget(self.btneq)

        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h7)
        self.v1.addLayout(self.h8)

        self.setLayout(self.v1)
        self.setStyleSheet('''QWidget {
    background-color: #2d2d2d;
    color: #ffffff;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 18px;
    border: none;
}

/* Стиль для QLineEdit (дисплей калькулятора) */
QLineEdit {
    background-color: #1e1e1e;
    color: #ffffff;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 10px;
    font-size: 32px;
    font-weight: light;
    qproperty-alignment: AlignRight;
    selection-background-color: #0078d7;
    selection-color: #ffffff;
}

/* Стиль для кнопок */
QPushButton {
    background-color: #2d2d2d;
    color: #ffffff;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 12px 0;
    font-size: 18px;
    min-width: 60px;
}

/* Стиль для кнопок при наведении */
QPushButton:hover {
    background-color: #3a3a3a;
    border: 1px solid #4a4a4a;
}

/* Стиль для кнопок при нажатии */
QPushButton:pressed {
    background-color: #1e1e1e;
    border: 1px solid #2a2a2a;
}

/* Стиль для числовых кнопок */
QPushButton[class="number"] {
    background-color: #2d2d2d;
    font-weight: normal;
}

/* Стиль для операторов (+, -, *, /) */
QPushButton[class="operator"] {
    background-color: #1a1a1a;
    color: #ff9500;
    font-size: 20px;
}

/* Стиль для кнопки равно (=) */
QPushButton[class="equals"] {
    background-color: #ff9500;
    color: #ffffff;
    font-size: 20px;
}

/* Стиль для специальных кнопок (C, CE, ←, %, ±) */
QPushButton[class="special"] {
    background-color: #1a1a1a;
    color: #ffffff;
    font-size: 16px;
}

/* Стиль для кнопки памяти (MC, MR, MS, M+, M-) */
QPushButton[class="memory"] {
    background-color: #1a1a1a;
    color: #a0a0a0;
    font-size: 14px;
    padding: 8px 0;
}''')
        self.show()
    def noll(self):
        self.lbl.setText("")
        self.inpt.setText("")
        self.token = ("")
    def eq(self):
        self.lbl.setText(self.inpt.text())
        try:
            x = str(eval(self.inpt.text()))
            self.inpt.setText(x)
        except:
            self.noll
            return None
        '''def perc(self):
            x = int(self.lbl.text())
            a = '''
    def add_scoba(self):
        if self.scobka == True:
            root.inpt.setText(root.inpt.text() + ")")
        if self.scobka == False:
            root.inpt.setText(root.inpt.text() + "(")
        self.scobka = not self.scobka
    def sqr(self):
        self.lbl.setText(self.inpt.text() + "²")
        try:
            x = str(eval(self.inpt.text())**2)
            self.inpt.setText(x)
        except:
            self.noll
            return None
    def cb(self):
        self.lbl.setText(self.inpt.text() + "³")
        try:
            x = str(eval(self.inpt.text())**3)
            self.inpt.setText(x)
        except:
            self.noll
            return None
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.inpt.setText(self.inpt.text()+str(1))
        if event.key() == Qt.Key_2:
            self.inpt.setText(self.inpt.text()+str(2))
        if event.key() == Qt.Key_3:
             self.inpt.setText(self.inpt.text()+str(3))
        if event.key() == Qt.Key_4:
            self.inpt.setText(self.inpt.text()+str(4))
        if event.key() == Qt.Key_5:
            self.inpt.setText(self.inpt.text()+str(5))
        if event.key() == Qt.Key_6:
            self.inpt.setText(self.inpt.text()+str(6))
        if event.key() == Qt.Key_7:
            self.inpt.setText(self.inpt.text()+str(7))
        if event.key() == Qt.Key_8:
            self.inpt.setText(self.inpt.text()+str(8))
        if event.key() == Qt.Key_9:
            self.inpt.setText(self.inpt.text()+str(9))
        if event.key() == Qt.Key_0:
            self.inpt.setText(self.inpt.text()+str(0))
        self.inpt.setText(self.inpt.text()[0:32])



        

class btn_nums(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.clicked.connect(self.add_letter)
    def add_letter(self):
        root.inpt.setText(root.inpt.text() + self.text())
         
class btn_func(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.clicked.connect(self.add_letter)
    def add_letter(self):
        root.inpt.setText(root.inpt.text() + self.text())

root = window()


app.exec_()






