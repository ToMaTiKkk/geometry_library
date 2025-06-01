import pytest
import math
from geometry_lib import Circle, NonPositiveValueError, Shape

class TestCircle:
    def test_circle_creation_valid_radius(self):
        circle = Circle(5.0)
        assert circle.radius == 5.0
        assert isinstance(circle, Shape)
        
    def test_circle_creation_zero_radius(self):
        with pytest.raises(NonPositiveValueError):
            Circle(0)
            
    def test_circle_creation_negative_radius(self):
        with pytest.raises(NonPositiveValueError):
            Circle(-5.0)
            
    def test_circle_creation_invelid_type(self):
        with pytest.raises(TypeError):
            Circle("Пять")
        
    def test_circle_area_calculation(self):
        circle = Circle(10.0)
        assert circle.area() == pytest.approx(math.pi * 100)
        
    def test_circle_str_repr(self):
        circle = Circle(3)
        assert str(circle) == "Круг с радиусом 3.0"
        assert repr(circle) == "Circle(radius=3.0)"