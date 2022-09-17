from ast import main
import unittest

from main import Main


class TestStudent(unittest.TestCase):
    def test_calculate(self):
        main = Main()
