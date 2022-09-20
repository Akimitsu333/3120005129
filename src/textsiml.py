import sys
import jieba
import Levenshtein


class TextSiml:
    def __init__(self, paths=None):
        self.paths = paths
        self.files = None
        self.strs = None
        self.result = None

    def getPath(self):
        if self.paths == None:
            if len(sys.argv) != 4:
                print(
                    "Format error! Please enter in the following format: \n\tpython main.py [原文文件] [抄袭版论文的文件] [答案文件]"
                )
            else:
                self.paths = sys.argv[1:4]
        return True

    def openFile(self):
        try:
            orig_file = open(self.paths[0], mode="r", encoding="utf-8")
            siml_file = open(self.paths[1], mode="r", encoding="utf-8")
            rst_file = open(self.paths[2], mode="w", encoding="utf-8")
        except IOError as e:
            print("Error opening file: ", e)
        print("File opened successfully.")
        self.files = orig_file, siml_file, rst_file
        return True

    def closeFile(self):
        for file in self.files:
            file.close()
        print("File saved successfully.")
        return True

    def readFile(self):
        orig_str = self.files[0].read()
        siml_str = self.files[1].read()
        print("File read successfully.")
        self.strs = orig_str, siml_str
        return True

    def writeFile(self):
        self.files[2].write(str(self.result))
        print("File written successfully.")
        return True

    def calculate(self):
        # 分词
        orig = jieba.lcut(self.strs[0])
        siml = jieba.lcut(self.strs[1])
        # 计算相似度
        result = Levenshtein.ratio(orig, siml)
        # 四舍五入到小数点后两位
        self.result = round(result, 2)
        # 输出相似度
        print("Similarity calculation succeeded: {0}".format(self.result))
        return True

    def start(self):
        self.getPath()
        self.openFile()
        self.readFile()
        self.calculate()
        self.writeFile()
        self.closeFile()

        return True
