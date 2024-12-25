"""Модуль, на который ссылается программа во время валидации"""
from exceptions import ColorError, LengthError
from PyQt5.QtWidgets import QMessageBox

class Validation(QMessageBox):
    def _validate_background(self, background):
        """Проверка фона(все открытки)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(background) not in colors: #Проверка на попадание цвета фона в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета фона! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_snow(self, snow):
        """Проверка цвета снега(открытка 1)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(snow) not in colors: #Проверка на попадание цвета снега в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета снега! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_snowman(self, snowman):
        """Проверка цвета снеговика(открытка 1)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(snowman) not in colors: #Проверка на попадание цвета снеговика в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета снеговика! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_extra(self, extra):
        """Проверка цвета ведра(открытки 1 и 2)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(extra) not in colors: #Проверка на попадание цвета ведра в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета ведра! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_floor(self, floor):
        """Проверка цвета пола(открытка 2)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(floor) not in colors: #Проверка на попадание цвета пола в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета пола! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_tree(self, tree):
        """Проверка цвета ёлки(открытка 2)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(tree) not in colors: #Проверка на попадание цвета ёлки в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета ёлки! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_snowfall(self, snow_c):
        """Проверка цвета снежинки(открытка 3)"""
        colors = ['белый', 'чёрный', 'синий', 'красный', 'зелёный', 'серый', 'розовый', 'голубой', 'жёлтый',
                  'коричневый']
        try:
            if str(snow_c) not in colors: #Проверка на попадание цвета снежинки в доступные
                raise ColorError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты допустил ошибку при вводе цвета снежинки! Проверь еще раз")
            self.msg.show()
            return 0

    def _validate_name(self, name):
        """Проверки имени на количество символов(все открытки)"""
        try:
            if len(str(name)) > 15: #Проверка на длину имени получателя
                raise LengthError
            return 1
        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Ошибка ввода")
            self.msg.setText("Ты ввёл слишком длинное имя получателя! Проверь еще раз")
            self.msg.show()
            return 0