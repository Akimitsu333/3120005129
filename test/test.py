from ast import main
import unittest

from 第二次作业.src.main import Main


class TestStudent(unittest.TestCase):
    def test_calculate(self):
        main = Main()
        print(main.calculate("abc", "abb"))
