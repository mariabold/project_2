"""Создание открытки со снежинкой"""
from PIL import Image, ImageDraw, ImageFont
from validation import Validation
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class Snow(QWidget):
    def __init__(self, *args):
        """реализация окна с выбором цветов и получателя"""
        super().__init__()
        uic.loadUi('draw_snowfall.ui', self)
        self.setWindowTitle('Характеристики снежинки')
        self.create_button3.clicked.connect(self.check_inf) #Кнопка, запускающая валидацию и отрисовку
        self.back = (self.back_color.text()).lower()
        self.snow = (self.snowfall_color.text()).lower()
        self.named = self.name_inf.text()
        self.msg = QMessageBox() #Финальное диалоговое окна после создания октрытки
        self.msg.setWindowTitle("Открытка готова")

    def check_inf(self):
        """Валидация аргументов через функции из validation"""
        self.back = (self.back_color.text()).lower()
        self.snow = (self.snowfall_color.text()).lower()
        self.named = self.name_inf.text()
        flag = 0
        flag += Validation._validate_background(self, self.back) #Валидация аргументов
        flag += Validation._validate_snowfall(self, self.snow)
        flag += Validation._validate_name(self, self.named)
        if flag == 3:
            self.draw_snowing() #Если все валидации пройдены, запуск отрисовки

    def draw_snowing(self):
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
        self.background_c = self.colours[self.back] #перевод цветов в rgb
        self.snow_c = self.colours[self.snow]
        picture = Image.new('RGB', (400, 400), self.background_c)  # Отрисовка снежинки
        draw = ImageDraw.Draw(picture)
        draw.line(((200, 75), (200, 375)), fill=self.snow_c, width=20)
        draw.line(((50, 225), (350, 225)), fill=self.snow_c, width=20)
        draw.line(((87, 112), (313, 338)), fill=self.snow_c, width=20)
        draw.line(((87, 338), (313, 112)), fill=self.snow_c, width=20)
        draw.ellipse((170, 195, 230, 255), fill=self.snow_c)
        draw.ellipse((180, 205, 220, 245), fill=self.background_c)
        font = ImageFont.truetype('font.ttf', size=25, encoding='UTF-8')
        draw.text((100, 10), "Happy New Year,", font=font, fill='black')
        draw.text((100, 40), f'{self.named}!', font=font, fill='black')
        picture.save('NewYear.jpg', 'JPEG')
        options = QFileDialog.Options() #Возможность сохранения с пользовательским названием в любую папку
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить картинку", "", "Изображения (*.png *.jpg *.bmp);;Все файлы (*)", options=options)
        if file_name:
            pixmap = QPixmap("NewYear.jpg")
            pixmap.save(file_name)
        self.msg.setText('Твоя открытка сохранена! Порадуй ею своих близких!') #Вывод финального окна
        self.msg.show()