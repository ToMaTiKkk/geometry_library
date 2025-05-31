import pytest
import math
from geometry_lib import Triangle, NonPositiveValueError, TriangleInequalityError, Shape

class TestTriangle:
    def test_triangle_creation_valid(self):
        t = Triangle(3, 4, 5)
        assert (t.side_a, t.side_b, t.side_c) == (3.0, 4.0, 5.0)
        assert isinstance(t, Shape)
        
    @pytest.mark.parametrize("s1,s2,s3", [(1,2,10), (1,1,0), (1,-1,1)])
    def test_triangle_creation_invalid_params(self, s1, s2, s3):
        if s3 <= 0 or s2 <= 0 or s1 <= 0:
            with pytest.raises(NonPositiveValueError):
                Triangle(s1, s2, s3)
        else:
            with pytest.raises(TriangleInequalityError):
                Triangle(s1, s2, s3)
                
    def test_triangle_creation_type(self):
        with pytest.raises(TypeError):
            Triangle(3, 4, "5")
            
    def test_triangle_area_3_4_5(self):
        t = Triangle(3, 4, 5)
        assert t.area() == pytest.approx(6.0)
        
    def test_is_right_angled_3_4_5(self):
        t = Triangle(3, 4, 5)
        assert t.is_right_angled() is True
        
    def test_is_right_angled_not_right(self):
        t = Triangle(2, 3, 4)
        assert t.is_right_angled() is False
        
    def test_triangle_str_repr(self):
        t =Triangle(1.1, 2.2, 3.0)
        assert str(t) == "Треугольник со сторонами 1.1, 2.2, 3.0"
        assert repr(t) == "Triangle(side_a=1.1, side_b=2.2, side_c=3.0)"