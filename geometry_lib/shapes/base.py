from abc import ABC, abstractmethod

# базовый и абстрактный класс для геом фигур
class Shape(ABC):
    # вычисляет и возвращает площадь фигуры
    @abstractmethod
    def area(self) -> float:
        pass
        
    # вовзращает строковое представление объекта фигуры
    def __str__(self) -> str:
        return self.__str__.__name__