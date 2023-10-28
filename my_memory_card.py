#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QRushButton, QLabel)
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')



btn_ok = QRushButton('Ответить')
Ib_Question = QLabel('в каком году была основана Москва?')












R = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QHVBoxLayout()

layout_ans2.addwidget(rbtn_1)
layout_ans2.addwidget(rbtn_2)
layout_ans3.addwidget(rbtn_3)
layout_ans3.addwidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(Id_Question, alignment=(Qt.alignHCenter / Qt.AlignVCenter))




