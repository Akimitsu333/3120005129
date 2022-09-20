import unittest
from unittest import result
import textsiml
import sys


class TestStudent(unittest.TestCase):
    def test_init(self):
        t1 = textsiml.TextSiml()
        self.assertEqual(t1.paths, None)
        self.assertEqual(t1.files, None)
        self.assertEqual(t1.strs, None)
        self.assertEqual(t1.result, None)
        pass

    def test_get_path(self):
        t1 = textsiml.TextSiml()
        self.assertFalse(t1.get_path())  # 空参数会报错
        sys.argv = [
            "main.py",
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        ]
        self.assertTrue(t1.get_path())  # 参数数量正确,获取路径值正常
        pass

    def test_open_file(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
        )
        self.assertTrue(t1.open_file())  # 文件存在,打开正常
        t1.close_file()
        t1.paths = (
            "source/aaa",
            "source/bbb",
        )
        self.assertFalse(t1.open_file())  # 文件不存在,报错且返回False

        pass

    def test_close_file(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        t1.open_file()
        self.assertTrue(t1.close_file())  # 文件关闭正常
        pass

    def test_read_file(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
        )
        t1.open_file()
        self.assertTrue(t1.read_file())  # 文件读取正常
        t1.close_file()
        pass

    def test_write_file(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        t1.result = 0.80  # 测试文本,可随机
        self.assertTrue(t1.write_file())  # 文件写入正常

        pass

    def test_calculate(self):
        t1 = textsiml.TextSiml()
        t1.strs = ("我们的班级", "我们班级")
        self.assertTrue(t1.calculate())  # 计算运行正常
        print(t1.result)
        self.assertEqual(t1.result, 0.8)  # 测试结果符合预期
        pass

    def test_start(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        self.assertTrue(t1.start())  # 模块启动正常
        pass

    # def test_(self):
    #     """保留的可拓展函数"""
    #     pass


# 入口
if __name__ == "__main__":
    unittest.main()
