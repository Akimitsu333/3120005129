import unittest
import cProfile
from memory_profiler import profile

from main import Main


class TestStudent(unittest.TestCase):
    def test_time(self):
        cProfile.run(
            Main().start(
                "source/orig.txt", "source/orig_0.8_add.txt", "source/result.txt"
            )
        )

    @profile
    def test_memory(self):
        Main().start("source/orig.txt", "source/orig_0.8_add.txt", "source/result.txt")
