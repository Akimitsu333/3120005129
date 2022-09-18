import sys
import jieba
import Levenshtein


class TextSiml:
    def getPath(self):
        if len(sys.argv) != 4:
            print(
                "Format error! Please enter in the following format: \n\tpython main.py [原文文件] [抄袭版论文的文件] [答案文件]"
            )
        return sys.argv[1:4]

    def openFile(self, paths):
        try:
            orig_file = open(paths[0], mode="r", encoding="utf-8")
            siml_file = open(paths[1], mode="r", encoding="utf-8")
            rst_file = open(paths[2], mode="w", encoding="utf-8")
        except IOError as e:
            print("Error opening file: ", e)
        print("File opened successfully!")
        return orig_file, siml_file, rst_file

    def closeFile(self, files):
        for file in files:
            file.close()
        print("File saved successfully!")

    def readFile(self, files):
        orig_str = files[0].read()
        siml_str = files[1].read()
        print("File read successfully!")
        return orig_str, siml_str

    def writeFile(self, files, str):
        files[2].write(str)
        print("File written successfully!")

    def calculate(self, strs):

        # 分词
        orig = jieba.lcut(strs[0])
        siml = jieba.lcut(strs[1])

        # 计算相似度
        result = Levenshtein.ratio(orig, siml)
        # 转化为百分比
        result = result * 100
        print("Similarity calculation succeeded: {0:.1f}%".format(result))
        return result

    def start(self):
        paths = self.getPath()
        files = self.openFile(paths)
        txts = self.readFile(files)
        result = self.calculate(txts)
        self.writeFile(
            files,
            "The similarity between {0} and {1} is: {2:.1f}%".format(
                paths[0], paths[1], result
            ),
        )
        self.closeFile(files)
