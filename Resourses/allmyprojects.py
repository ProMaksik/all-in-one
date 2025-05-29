from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPixmap
from pygame import *
import subprocess


app = QApplication([])

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("МОИ ЛУЧШИЕ ПРОЕКТЫ")

        self.label = QLabel("МОИ ПРОЕКТЫ")
        self.btnlabirint = QPushButton("Открыть игру 'Лабиринт'")
        self.btnlabirint.clicked.connect(lambda: subprocess.run(["python","Resourses/apps/labirint/labirint.py"]))
        self.btnfastclcik = QPushButton("Открыть игру 'Фаст Кликер'")
        self.btnfastclcik.clicked.connect(lambda: os.system("fastclicker.py"))
        self.btncalculator = QPushButton("Открыть калькулятор")
        self.btncalculator.clicked.connect(lambda: os.system("calculator.py"))

        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.v = QVBoxLayout()

        self.pixmapcal = QPixmap("Resourses\pictures\Калькулятор.png")
        self.pixmapfast = QPixmap("Resourses\pictures\фасткликер.png")
        self.pixmaplab = QPixmap("Resourses\pictures\лабиринт.png")

        self.pixmapcal = self.pixmapcal.scaled(self.pixmapcal.width(), self.pixmapcal.height())
        self.pixmapfast = self.pixmapfast.scaled(self.pixmapfast.width(), self.pixmapfast.height())
        self.pixmaplab = self.pixmaplab.scaled(self.pixmaplab.width(), self.pixmaplab.height())
        
        self.lblcal = QLabel()
        self.lblfast = QLabel()
        self.lbllab = QLabel()

        self.lblcal.setPixmap(self.pixmapcal)
        self.lblfast.setPixmap(self.pixmapfast)
        self.lbllab.setPixmap(self.pixmaplab)

        self.h1.addWidget(self.label, alignment= Qt.AlignCenter)
        self.h2.addWidget(self.lblcal)
        self.h2.addWidget(self.lblfast)
        self.h2.addWidget(self.lbllab)
        self.h3.addWidget(self.btncalculator)
        self.h3.addWidget(self.btnfastclcik)
        self.h3.addWidget(self.btnlabirint)

        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.v.addLayout(self.h3)


        self.setLayout(self.v)
        self.setStyleSheet('''/* Основной стиль для темной темы */
QWidget {
    background-color: #2d2d2d;
    color: #e0e0e0;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 12px;
    border: none;
}

/* Стиль для кнопок */
QPushButton {
    background-color: #3a3a3a;
    border: 1px solid #4a4a4a;
    border-radius: 4px;
    padding: 5px 10px;
    min-width: 80px;
}

QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #5a5a5a;
}

QPushButton:pressed {
    background-color: #2a2a2a;
}

QPushButton:disabled {
    background-color: #333333;
    color: #777777;
}

/* Стиль для текстовых полей */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #333333;
    border: 1px solid #444444;
    border-radius: 3px;
    padding: 5px;
    selection-background-color: #505050;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #5a5a5a;
}

/* Стиль для списков и таблиц */
QListView, QTreeView, QTableView {
    background-color: #333333;
    border: 1px solid #444444;
    alternate-background-color: #3a3a3a;
}

QHeaderView::section {
    background-color: #3a3a3a;
    color: #e0e0e0;
    padding: 5px;
    border: none;
}

/* Стиль для вкладок */
QTabWidget::pane {
    border: 1px solid #444444;
}

QTabBar::tab {
    background-color: #3a3a3a;
    color: #e0e0e0;
    padding: 5px 10px;
    border: 1px solid #444444;
    border-bottom: none;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:selected {
    background-color: #2d2d2d;
    border-bottom: 1px solid #2d2d2d;
}

QTabBar::tab:hover {
    background-color: #4a4a4a;
}

/* Стиль для чекбоксов и радиокнопок */
QCheckBox, QRadioButton {
    spacing: 5px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    background-color: #333333;
    border: 1px solid #555555;
}

QCheckBox::indicator:checked {
    background-color: #505050;
    border: 1px solid #555555;
    image: url(:/icons/checkmark.png);
}

QRadioButton::indicator:unchecked {
    background-color: #333333;
    border: 1px solid #555555;
    border-radius: 8px;
}

QRadioButton::indicator:checked {
    background-color: #505050;
    border: 1px solid #555555;
    border-radius: 8px;
}

/* Стиль для ползунков */
QSlider::groove:horizontal {
    height: 6px;
    background-color: #3a3a3a;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    width: 14px;
    height: 14px;
    background-color: #606060;
    border-radius: 7px;
    margin: -4px 0;
}

QSlider::sub-page:horizontal {
    background-color: #505050;
    border-radius: 3px;
}

/* Стиль для выпадающих списков */
QComboBox {
    background-color: #333333;
    border: 1px solid #444444;
    border-radius: 3px;
    padding: 5px;
    min-width: 100px;
}

QComboBox:hover {
    border: 1px solid #5a5a5a;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #444444;
}

QComboBox::down-arrow {
    image: url(:/icons/down_arrow.png);
}

QComboBox QAbstractItemView {
    background-color: #333333;
    color: #e0e0e0;
    border: 1px solid #444444;
    selection-background-color: #505050;
}

/* Стиль для разделителей */
QSplitter::handle {
    background-color: #444444;
    width: 4px;
    height: 4px;
}

/* Стиль для меню */
QMenuBar {
    background-color: #2d2d2d;
    color: #e0e0e0;
    border-bottom: 1px solid #444444;
}

QMenuBar::item {
    padding: 5px 10px;
    background-color: transparent;
}

QMenuBar::item:selected {
    background-color: #3a3a3a;
}

QMenu {
    background-color: #333333;
    border: 1px solid #444444;
    padding: 5px;
}

QMenu::item:selected {
    background-color: #505050;
}

QMenu::separator {
    height: 1px;
    background-color: #444444;
    margin: 3px 0;
}

/* Стиль для статус-бара */
QStatusBar {
    background-color: #2d2d2d;
    border-top: 1px solid #444444;
    color: #a0a0a0;
}

/* Стиль для прокрутки */
QScrollBar:vertical, QScrollBar:horizontal {
    background-color: #333333;
    width: 12px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #4a4a4a;
    min-height: 20px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background-color: #5a5a5a;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
}

QScrollBar::add-page, QScrollBar::sub-page {
    background: none;
}''')
        self.show()

root = Windows()

app.exec_()