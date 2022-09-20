import sys
import jieba
import Levenshtein


class TextSiml:
    def __init__(self):
        """初始化全局变量

        Args:
            paths (tuple, optional): 默认文件路径参数,用于解决非命令行参数启动模块时无法获取路径的问题. Defaults to None.
        """
        self.paths = None
        self.strs = None
        self.result = None

    def get_path(self):
        """判断路径是否正确传入

        Returns:
            True: 函数正确执行完毕
        """
        if len(sys.argv) != 4:
            raise Exception(
                "Format error! Please enter in the following format: \n\tpython main.py [原文文件] [抄袭版论文的文件] [答案文件]"
            )
        else:
            self.paths = sys.argv[1:4]
            return True

    def read_file(self):
        """尝试打开路径对应的文件对象并读入其中的文本

        Returns:
            True: 函数正确执行完毕
        """
        try:  # 尝试能否操作所有路径对应的文件
            with open(self.paths[0], mode="r", encoding="utf-8") as f:
                orig_str = f.read()
            with open(self.paths[1], mode="r", encoding="utf-8") as f:
                siml_str = f.read()
            with open(self.paths[2], mode="w", encoding="utf-8") as f:
                pass
        except IOError:
            raise IOError("Error opening file!Try again!")

        print("File read successfully.")
        self.strs = orig_str, siml_str  # 保存读取的文本

        return True

    def write_file(self):
        """将结果写入文件result.txt

        Returns:
            True: 函数正确执行完毕
        """
        with open(self.paths[2], "w") as f:
            f.write("{0:.2f}".format(self.result))  # 强制保留两位小数
        print("File written successfully.")

        return True

    def calculate(self):
        """计算相似度

        Returns:
            True: 函数正确执行完毕
        """
        jieba_tokenizer = jieba.Tokenizer()  # 重定向jieba分词的cache
        jieba_tokenizer.tmp_dir = "./"
        jieba_tokenizer.cache_file = self.paths[2]

        orig_words = jieba_tokenizer.lcut(self.strs[0])  # 分词
        siml_words = jieba_tokenizer.lcut(self.strs[1])

        self.result = Levenshtein.ratio(orig_words, siml_words)  # 计算相似度
        print(
            "Similarity calculation succeeded: {0:.2f}".format(self.result)
        )  # 以两位小数打印相似度

        return True

    def start(self):
        """启动模块

        Returns:
            True: 函数正确执行完毕
        """
        self.get_path()  # 依次启动各功能
        self.read_file()
        self.calculate()
        self.write_file()

        return True
