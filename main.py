from PyQt6.QtWidgets import *
import random

app = QApplication([])
window = QWidget()
window.resize(500, 500)
main_line = QVBoxLayout()


text = QLabel("Рандомайзер переможця")
button = QPushButton('Визначити переможця')
winner_lbl = QLabel('?')
user_check = QFontComboBox()

main_line.addWidget(text)
main_line.addWidget(button)
main_line.addWidget(winner_lbl)
main_line.addWidget(user_check)

def winner():
    w = random.randint(1, 100)
    winner_lbl.setText(str(w))

window.setLayout(main_line)
button.clicked.connect(winner)
window.show()
app.exec()
