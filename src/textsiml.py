import sys
import jieba
import Levenshtein


class TextSiml:
    def __init__(self, paths: tuple = None):
        """初始化全局变量

        Args:
            paths (tuple, optional): 默认文件路径参数,用于解决非命令行参数启动模块时无法获取路径的问题. Defaults to None.
        """
        self.paths = paths
        self.files = None
        self.strs = None
        self.result = None

    def get_path(self):
        """判断路径是否存在/传入

        Returns:
            False: 执行过程出错
            True: 函数正确执行完毕
        """
        if self.paths == None:  # 默认路径优先级高于命令行传入参数
            if len(sys.argv) != 4:
                print(
                    "Format error! Please enter in the following format: \n\tpython main.py [原文文件] [抄袭版论文的文件] [答案文件]"
                )
                return False
            else:
                self.paths = sys.argv[1:4]
                return True

    def open_file(self):
        """尝试打开路径对应的文件对象

        Returns:
            False: 执行过程出错
            True: 函数正确执行完毕
        """
        try:
            orig_file = open(self.paths[0], mode="r", encoding="utf-8")
            siml_file = open(self.paths[1], mode="r", encoding="utf-8")
            rst_file = open(self.paths[2], mode="w", encoding="utf-8")
        except IOError as e:
            print("Error opening file: ", e)
            return False

        print("File opened successfully.")
        self.files = orig_file, siml_file, rst_file  # 记录打开的文件对象

        return True

    def close_file(self):
        """关闭打开的文件对象

        Returns:
            True: 函数正确执行完毕
        """
        for file in self.files:  # 关闭所有打开的文件对象
            file.close()
        print("File saved successfully.")

        return True

    def read_file(self):
        """读取待比较文件的内容

        Returns:
            True: 函数正确执行完毕
        """
        orig_str = self.files[0].read()  # 读取原文和抄袭
        siml_str = self.files[1].read()
        print("File read successfully.")
        self.strs = orig_str, siml_str

        return True

    def write_file(self):
        """将结果写入文件result.txt

        Returns:
            True: 函数正确执行完毕
        """
        self.files[2].write(str(self.result))
        print("File written successfully.")

        return True

    def calculate(self):
        """计算相似度

        Returns:
            True: 函数正确执行完毕
        """
        # 分词
        orig_words = jieba.lcut(self.strs[0])
        siml_words = jieba.lcut(self.strs[1])
        # 计算相似度
        result = Levenshtein.ratio(orig_words, siml_words)
        # 四舍五入到小数点后两位
        self.result = round(result, 2)
        # 输出相似度
        print("Similarity calculation succeeded: {0}".format(self.result))

        return True

    def start(self):
        """启动模块

        Returns:
            True: 函数正确执行完毕
        """
        self.get_path()  # 依次启动各功能
        self.open_file()
        self.read_file()
        self.calculate()
        self.write_file()
        self.close_file()

        return True
