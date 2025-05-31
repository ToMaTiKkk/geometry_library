import pytest
import math
from geometry_lib import create_shape, Circle, Triangle, Shape, NonPositiveValueError

class TestFactoryAndPolymorphism:
    def test_create_circle_positional(self):
        shape = create_shape(5.0)
        assert isinstance(shape, Circle)
        assert shape.radius == 5.0
        
    def test_create_circle_keyword(self):
        shape = create_shape(radius=10)
        assert isinstance(shape, Circle)
        assert shape.radius == 10.0
        
    def test_create_triangle_positional(self):
        shape = create_shape(3.0, 4.0, 5.0)
        assert isinstance(shape, Triangle)
        
    def test_create_triangle_keyword(self):
        shape = create_shape(side_a=7, side_b=10, side_c=12)
        assert isinstance(shape, Triangle)
        
    def test_create_shape_unknown_raises_value_error(self):
        with pytest.raises(ValueError):
            create_shape(1.0, 2.0)
        with pytest.raises(ValueError):
            create_shape()
            
    def test_create_shape_propagates_errors(self):
        with pytest.raises(NonPositiveValueError):
            create_shape(radius=0)
            
    def test_polymorphic_area_calculation(self):
        shapes: list[Shape] = [create_shape(radius=1.0), create_shape(3.0, 4.0, 5.0)]
        expected_areas = [math.pi, 6.0]
        for i, shape_item in enumerate(shapes):
            assert shape_item.area() == pytest.approx(expected_areas[i])