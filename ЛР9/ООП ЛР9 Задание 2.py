import math

class ПрямоугольныйТреугольник:
    def __init__(self, катет1, катет2):
        self.катет1 = катет1
        self.катет2 = катет2

    def вычислить_площадь(self):
        return 0.5 * self.катет1 * self.катет2

class ПроизвольныйТреугольник:
    def __init__(self, сторона1, сторона2, сторона3):
        self.сторона1 = сторона1
        self.сторона2 = сторона2
        self.сторона3 = сторона3

    def вычислить_площадь(self):
        # Используем формулу Герона для вычисления площади треугольника
        s = (self.сторона1 + self.сторона2 + self.сторона3) / 2
        return math.sqrt(s * (s - self.сторона1) * (s - self.сторона2) * (s - self.сторона3))

# Создание объектов классов
прямоугольный_треугольник = ПрямоугольныйТреугольник(3, 4)
произвольный_треугольник = ПроизвольныйТреугольник(5, 6, 7)

# Вызов полиморфных методов
площадь_прямоугольного_треугольника = прямоугольный_треугольник.вычислить_площадь()
площадь_произвольного_треугольника = произвольный_треугольник.вычислить_площадь()

# Вывод результатов
print(f"Площадь прямоугольного треугольника: {площадь_прямоугольного_треугольника}")
print(f"Площадь произвольного треугольника: {площадь_произвольного_треугольника}")