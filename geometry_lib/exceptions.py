# базовое исключение ошибок библиотеки
class ShapeError(Exception):
    pass
    
# некорректные параметры геометрич
class InvalidShapeParametersError(ShapeError, ValueError):
    pass
    
class NonPositiveValueError(InvalidShapeParametersError):
    def __init__(self, parameter_name: str, value: float | int):
        super().__init__(f"Параметр {parameter_name} должен быть положительным число. Получено: {value}")
        self.parameter_name = parameter_name
        self.value = value
    
# стороны не образуют треугол    
class TriangleInequalityError(InvalidShapeParametersError):
    def __init__(self, a: float, b: float, c: float):
        super().__init__(f"Стороны {a}, {b}, {c} не могут образовать треугольник. Сумма длин двух любых должна быть строго больше третьей стороны.")
        self.sides = (a, b, c)