"""Окно выбора типа открытки, переход к следующим модулям"""
from snowman import Snowman
from tree import Tree
from snowing import Snow
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Drawing(QWidget):
    def __init__(self, *args):
        """Создание окна"""
        super().__init__()
        uic.loadUi('choosing.ui', self)
        self.setWindowTitle('Выбери рисунок')
        self.snowman_button.clicked.connect(self.to_draw_snowman) #Кнопка для создания открытки со снеговиком
        self.tree_button.clicked.connect(self.draw_a_christmas_tree) #Кнопка для создания открытки с ёлкой
        self.ice_button.clicked.connect(self.draw_snowing) #Кнопка для создания открытки со снежинкой

    def to_draw_snowman(self):
        """Переход к открытке со снеговиком"""
        self.draw_snowman = Snowman(self) #Запуск окна с вводом данных для отрисовки снеговика
        self.draw_snowman.show()

    def draw_a_christmas_tree(self):
        """Переход к открытке с ёлкой"""
        self.draw_tree = Tree(self) #Запуск окна с вводом данных для отрисовки ёлки
        self.draw_tree.show()

    def draw_snowing(self):
        """Переход к открытке со снежинкой"""
        self.draw_snow = Snow(self) #Запуск окна с вводом данных для отрисовки снежинки
        self.draw_snow.show()