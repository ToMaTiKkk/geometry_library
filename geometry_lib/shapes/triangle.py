import math
from .base import Shape
from ..exceptions import NonPositiveValueError, TriangleInequalityError    

class Triangle(Shape):
    _DEFAULT_TOLERANCE = 1e-9 # погрешность сравнения чисел, _* - для внутр использ
    
    # создаем сам объекта типа треугольник
    def __init__(self, side_a: float, side_b: float, side_c: float):
        sides = {"a": side_a,
                       "b": side_b,
                       "c": side_c
        }
        processed_sides: list[float] = []
        for name, length in sides.items():
            # сторона не явл числом
            if not isinstance(length, (int, float)):
                raise TypeError(f"Сторона '{name}' должна быть числом, тип: {type(length).__name__}.")
            if length <= 0:
                raise NonPositiveValueError(parameter_name=f"side_{name}", value=length)
            processed_sides.append(float(length))
        
        s_a, s_b, s_c = processed_sides
        all_sides_sorted = sorted([s_a, s_b, s_c])
        # нарушено условие существования треугольника
        if all_sides_sorted[0] + all_sides_sorted[1] <= all_sides_sorted[2]:
            raise TriangleInequalityError(s_a, s_b, s_c)
            
        self.side_a: float = s_a
        self.side_b: float = s_b
        self.side_c: float = s_c
    
    # считает площадь треугольника через формулу Герона    
    def area(self) -> float:
        s = (self.side_a + self.side_b + self.side_c) / 2
        area_sq = s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)
        if -self._DEFAULT_TOLERANCE < area_sq < 0:
            return 0.0
        return math.sqrt(area_sq)
      
    # проверка что прямоугольный, используя обратную теорему Пифагора  
    def is_right_angled(self, tolerance: float | None = None) -> bool:
        tol = tolerance if tolerance is not None else self._DEFAULT_TOLERANCE
        sides = [self.side_a, self.side_b, self.side_c]
        sides_sq = sorted([s**2 for s in sides])
        # сравниваем сумму квадратов двух меньших сторон с третьей, учитывая относит погрешность и абсолютную
        return math.isclose(sides_sq[0] + sides_sq[1], sides_sq[2], rel_tol=tol, abs_tol=tol) 
        
    def __repr__(self) -> str:
        return f"Triangle(side_a={self.side_a}, side_b={self.side_b}, side_c={self.side_c})"
        
    def __str__(self) -> str:
        return f"Треугольник со сторонами {self.side_a}, {self.side_b}, {self.side_c}"