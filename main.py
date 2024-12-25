"""В main.py реализуется запуск программы, создание главного окна и отсчёт до нового года"""
import sys
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from choice import Drawing


class Mainscreen(QMainWindow):
    def __init__(self):
        """Запуск основного окна"""
        super().__init__()
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle('Главная страница')
        self.make_button.clicked.connect(self.generator) #Кнопка перехода к генерации открыток
        self.Counter_button.clicked.connect(self.calendar) #Кнопка для информации о количестве дней до Нового года
        self.msg = QMessageBox() #Диалоговое окно с обратным отсчётом
        self.msg.setWindowTitle("Новогодний отсчет")

    def generator(self):
        """Запуск окна с выбором рисунка на открытке, переход к модулю choice"""
        self.drawing = Drawing(self) #Вызов окна с выбором темы октрытки
        self.drawing.show()

    def calendar(self):
        """Выводит диалоговое окно с отсчётом до Нового года или информацией, что он прошёл"""
        today = datetime.datetime.now().date() #Отсчёт дней до Нового года
        new_year = datetime.date(2025, 1, 1)
        num_days = (new_year - today).days
        if num_days > 0:
            self.msg.setText(f'Кстати, знаешь, сколько дней до Нового года? {num_days}! С наступающим!')
        else:
            self.msg.setText('Вообще-то Новый Год уже был) С прошедшим!') #Если нажать на кнопку после 1.01.25, то счётчик в минус пойдёт, альтернатива
        self.msg.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mainscreen()
    ex.show()
    sys.exit(app.exec_())