"""Создание открытки со снеговиком"""
from PIL import Image, ImageDraw, ImageFont
from validation import Validation
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

class Snowman(QWidget):
    def __init__(self, *args):
        """Вывод окна для выбора цвета"""
        super().__init__()
        uic.loadUi('drawingsnowman.ui', self)
        self.setWindowTitle('Характеристики снеговика')
        self.create_button1.clicked.connect(self.check_inf) #Кнопка для начала создания октрытки
        self.background =(self.background_color.text()).lower()
        self.snow = (self.snow_color.text()).lower()
        self.snowman = (self.snowman_color.text()).lower()
        self.extra = (self.extra_color.text()).lower()
        self.name_postcard = self.name.text()
        self.msg = QMessageBox() #Финальное окно
        self.msg.setWindowTitle("Открытка готова")

    def check_inf(self):
        """Обработка цветов и имени получателя, валидация"""
        self.background =(self.background_color.text()).lower() #Считывание данных для валидации
        self.snow = (self.snow_color.text()).lower()
        self.snowman = (self.snowman_color.text()).lower()
        self.extra = (self.extra_color.text()).lower()
        self.name_postcard = self.name.text()
        flag = 0
        flag += Validation._validate_background(self, self.background) #Валидация
        flag += Validation._validate_snow(self, self.snow)
        flag += Validation._validate_snowman(self, self.snowman)
        flag += Validation._validate_extra(self, self.extra)
        flag += Validation._validate_name(self, self.name_postcard)
        if flag == 5:
            self.draw_snowman() #Переход к отрисовке

    def draw_snowman(self):
        """Отрисовка открытки + сохранение"""
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
        self.back = self.colours[self.background]
        self.snow_c = self.colours[self.snow]
        self.snowman_c = self.colours[self.snowman]
        self.extra_c = self.colours[self.extra]
        self.picture = Image.new('RGB', (400, 500), self.back)  # Создание фона + снега
        self.draw = ImageDraw.Draw(self.picture)
        self.draw.polygon(((0, 500), (0, 350), (400, 350), (400, 500)), fill=self.snow_c)
        self.draw.line(((150, 250), (75, 326)), fill=(128, 64, 48), width=10)  # Отрисовка снеговика
        self.draw.line(((250, 250), (325, 326)), fill=(128, 64, 48), width=10)
        self.draw.ellipse((125, 275, 275, 425), fill=self.snowman_c, outline='black')
        self.draw.ellipse((137, 199, 263, 325), fill=self.snowman_c, outline='black')
        self.draw.ellipse((150, 125, 250, 225), fill=self.snowman_c, outline='black')
        self.draw.ellipse((175, 150, 191, 166), fill='black')
        self.draw.ellipse((209, 150, 225, 166), fill='black')
        self.draw.ellipse((175, 180, 225, 200), fill='black', outline='black')
        self.draw.polygon(((175, 175), (175, 190), (225, 190), (225, 175)), fill=self.snowman_c)
        self.draw.polygon(((160, 140), (170, 85), (230, 85), (240, 140)), fill=self.extra_c, outline='black')
        self.font = ImageFont.truetype('font.ttf', size=25, encoding='UTF-8')
        self.draw.text((100, 10), "Happy New Year,", font=self.font, fill='black')
        self.draw.text((100, 40), f'{self.name_postcard}!', font=self.font, fill='black')
        self.picture.save('NewYear.jpg', 'JPEG')
        options = QFileDialog.Options() #Сохранение открытки
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить картинку", "", "Изображения (*.png *.jpg *.bmp);;Все файлы (*)", options=options)
        if file_name:
            pixmap = QPixmap("NewYear.jpg")
            pixmap.save(file_name)
        self.msg.setText('Твоя открытка сохранена! Порадуй ею своих близких!') #Появление финального окна
        self.msg.show()