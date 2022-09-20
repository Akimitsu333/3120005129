import unittest

from textsiml import TextSiml


class TestStudent(unittest.TestCase):
    def test_time(self):
        # os.system(
        #     "python -m cProfile -s cumulative src/main.py source/orig.txt source/orig_0.8_add.txt source/result.txt"
        # )
        pass

    def test_memory(self):
        # os.system(
        #     "python -m memory_profiler src/main.py source/orig.txt source/orig_0.8_add.txt source/result.txt"
        # )
        pass


if __name__ == "__main__":
    unittest.main()
