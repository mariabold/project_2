"""Создание открытки с ёлкой"""
from PIL import Image, ImageDraw, ImageFont
from validation import Validation
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class Tree(QWidget):
    def __init__(self, *args):
        """Выведение окна для принятия аргументов, их инциализация"""
        super().__init__()
        uic.loadUi('christmas.ui', self)
        self.setWindowTitle('Характеристики ёлки')
        self.create_button2.clicked.connect(self.check_inf) #Кнопка начала валидации и отрисовки
        self.walls = (self.background.text()).lower()
        self.floor_color = (self.floor.text()).lower()
        self.chr_tree = (self.tree.text()).lower()
        self.bask = (self.basket.text()).lower()
        self.named = self.name.text()
        self.msg = QMessageBox() #Финальное окно после отрисовки и сохранения
        self.msg.setWindowTitle("Открытка готова")

    def check_inf(self):
        """Обрабатывает цвета и имя получателя, валидация"""
        self.walls = (self.background.text()).lower() #Считывание значений из строк ввода, привод к нижнему регистру для валидации
        self.floor_color = (self.floor.text()).lower()
        self.chr_tree = (self.tree.text()).lower()
        self.bask = (self.basket.text()).lower()
        self.named = self.name.text()
        flag = 0
        flag += Validation._validate_background(self, self.walls) #Валидация
        flag += Validation._validate_floor(self, self.floor_color)
        flag += Validation._validate_tree(self, self.chr_tree)
        flag += Validation._validate_extra(self, self.bask)
        flag += Validation._validate_name(self, self.named)
        if flag == 5:
            self.draw_tree() #Запуск отрисовки

    def draw_tree(self):
        """Отрисовка открытки и сохранение"""
        self.colours = {'белый': (255, 255, 255),
                  'чёрный': (0, 0, 0),
                  'синий': (0, 0, 255),
                  'красный': (255, 0, 0),
                  'зелёный': (0, 255, 0),
                  'серый': (128, 128, 128),
                  'розовый': (255, 192, 203),
                  'голубой': (0, 128, 255),
                  'жёлтый': (255, 255, 0),
                  'коричневый': (128, 64, 48)}
        self.wall = self.colours[self.walls] #Перевод в rgb
        self.fl = self.colours[self.floor_color]
        self.c_tree = self.colours[self.chr_tree]
        self.extra = self.colours[self.bask]
        picture = Image.new('RGB', (400, 500), self.wall)  # Отрисовка ёлки
        draw = ImageDraw.Draw(picture)
        draw.polygon(((0, 500), (0, 350), (400, 350), (400, 500)), fill=self.fl, outline='black')
        draw.polygon(((140, 425), (120, 325), (280, 325), (260, 425)), fill=self.extra, outline='black')
        draw.line(((200, 325), (200, 310)), fill='brown', width=30)
        draw.polygon(((90, 310), (310, 310), (200, 210)), fill=self.c_tree, outline='black')
        draw.polygon(((100, 220), (300, 220), (200, 130)), fill=self.c_tree, outline='black')
        draw.polygon(((110, 140), (290, 140), (200, 40)), fill=self.c_tree, outline='black')
        font = ImageFont.truetype('font.ttf', size=25, encoding='UTF-8')
        draw.text((100, 10), "Happy New Year,", font=font, fill='black')
        draw.text((100, 40), f'{self.named}!', font=font, fill='black')# Добавление надписи
        picture.save('NewYear.jpg', 'JPEG')
        options = QFileDialog.Options() #Сохранение картинки
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить картинку", "", "Изображения (*.png *.jpg *.bmp);;Все файлы (*)", options=options)
        if file_name:
            pixmap = QPixmap('NewYear.jpg')
            pixmap.save(file_name)
        self.msg.setText('Твоя открытка сохранена! Порадуй ею своих близких!')
        self.msg.show()