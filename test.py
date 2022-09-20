import unittest
import textsiml
import main
import sys


class TestStudent(unittest.TestCase):
    def test_init(self):
        t1 = textsiml.TextSiml()
        self.assertEqual(t1.paths, None)
        self.assertEqual(t1.strs, None)
        self.assertEqual(t1.result, None)

    def test_get_path_1(self):
        t1 = textsiml.TextSiml()
        sys.argv = [  # 模拟命令行参数
            "main.py",
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        ]
        self.assertTrue(t1.get_path())  # 参数数量正确,获取路径值正常

    def test_get_path_2(self):
        t1 = textsiml.TextSiml()
        sys.argv = ["aaa"]  # 模拟错误的命令行参数
        with self.assertRaises(Exception) as cm:  # 参数格式错误会报错
            t1.get_path()
        self.assertIsNotNone(cm.exception)  # 判断是否有报错

    def test_get_path_3(self):
        t1 = textsiml.TextSiml()
        sys.argv = ["no.1", "2", "3", "4", "5", "6"]  # 模拟错误的命令行参数
        with self.assertRaises(Exception) as cm:  # 参数格式错误会报错
            t1.get_path()
        self.assertIsNotNone(cm.exception)  # 判断是否有报错

    def test_read_file_1(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        self.assertTrue(t1.read_file())  # 文件存在,打开正常

    def test_read_file_2(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/aaa",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        with self.assertRaises(IOError) as cm:
            t1.read_file()
        self.assertIsNotNone(cm.exception)  # 文件不存在,会报错

    def test_read_file_3(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/bbb",
            "result.txt",
        )
        with self.assertRaises(IOError) as cm:
            t1.read_file()
        self.assertIsNotNone(cm.exception)  # 文件不存在,会报错

    def test_read_file_4(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "aaa/ccc",
        )
        with self.assertRaises(IOError) as cm:
            t1.read_file()
        self.assertIsNotNone(cm.exception)  # 文件不存在,会报错

    def test_write_file(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        t1.result = 0.80  # 测试文本,可随机
        self.assertTrue(t1.write_file())  # 文件写入正常

    def test_calculate(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        t1.strs = ("我们的班级", "我们班级")
        self.assertTrue(t1.calculate())  # 计算运行正常
        print(t1.result)
        self.assertEqual(t1.result, 0.8)  # 测试结果符合预期

    def test_start(self):
        t1 = textsiml.TextSiml()
        t1.paths = (
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        )
        self.assertTrue(t1.start())  # 模块启动正常

    def test_main(self):
        sys.argv = [  # 模拟命令行参数
            "main.py",
            "source/orig.txt",
            "source/orig_0.8_dis_1.txt",
            "result.txt",
        ]
        self.assertTrue(main.main())  # 测试主入口


# 入口
if __name__ == "__main__":
    unittest.main()
