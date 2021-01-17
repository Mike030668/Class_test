class Point2D:
    # """Точка на плоскости"""
    # Иницилизирующий метод (специальный метод с __)
    def __init__(self, x, y):
        self.x = x  # Поля читаются и записываются через 'self'
        self.y = y  # 'self' указывает на текущий класс
        # Обычный метод объекта(метод экземпляра класса)
        # имеет те же правила, наименования, что и обычные функции

    def __str__(self):
        return f'Точка: ({self.x}, {self.y})'
    # перегрузка  "+"
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def point_distance(self, a, b):
        return ((self.x - a) ** 2 + (self.y - b) ** 2)** 0.5


p = Point2D(2, 3)
q = Point2D(3, 4)


print(p.x, p.y)
print(p)
print(p.distance())

print(p.point_distance(3, 4))

print(p + q)
