import pytest
from Day1_Basics import Day1_Basics_Service

class TestAreaTriangle:
    def test_valid_input(self):
        assert Day1_Basics_Service.Area_Triangle(3,3) == 4.5

    def test_base_invalid(self):
        with pytest.raises(TypeError) as error_info: 
            Day1_Basics_Service.Area_Triangle('3', 4)
            print(error_info)
        assert str(error_info) == 'Value is not a Integer or Float'

    def test_area_invalid(self):
        pass

