from crypt import methods
import unittest
import textsiml


class TestStudent(unittest.TestCase):
    @methods
    def setUp(self) -> None:
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt ",
            "source/orig_0.8_dis_1.txt ",
            "source/result.txt",
        )
        return super().setUp()

    def test_init(self):
        t1 = textsiml.TextSiml()
        self.assertEqual(t1.paths, None)
        self.assertEqual(t1.files, None)
        self.assertEqual(t1.strs, None)
        self.assertEqual(t1.result, None)
        pass

    def test_get_path(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt ",
            "source/orig_0.8_dis_1.txt ",
            "source/result.txt",
        )
        self.assertTrue(t1.get_path())
        t2 = textsiml.TextSiml()
        self.assertFalse(t2.get_path())
        pass

    def test_open_file(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt ",
            "source/orig_0.8_dis_1.txt ",
            "source/result.txt",
        )

        pass

    def test_close_file(self):

        pass

    def test_read_file(self):

        pass

    def test_write_file(self):

        pass

    def test_calculate(self):

        pass

    def test_start(self):

        pass

    def test_(self):

        pass


# 入口
if __name__ == "__main__":
    unittest.main()
