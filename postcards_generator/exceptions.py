"""Класс исключений"""
class ColorError(Exception): #Цвет не из доступного списка
    pass

class LengthError(Exception): #Слишком длинное имя получателя
    pass