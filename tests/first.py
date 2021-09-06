import pytest
from app.Calculator import Calculator


class TestCAlc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correctly(self):
        assert self.calc.multiply(self, 3, 7) == 21

    def test_division_calc_correctly(self):
        assert self.calc.division(self, 20, 5) == 4

    def test_subtraction_calc_correctly(self):
        assert self.calc.subtraction(self, 37, 15) == 22

    def test_adding_calc_correctly(self):
        assert self.calc.adding(self, 7, 4) == 11
