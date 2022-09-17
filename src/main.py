import sys
import jieba
import jieba.analyse
import Levenshtein


class Main:
    def getPath(self):
        try:
            orig_path = sys.argv[1]
            siml_path = sys.argv[2]
            rst_path = sys.argv[3]
        except:
            print("格式错误！请按下列格式输入：\n\tpython main.py [原文文件] [抄袭版论文的文件] [答案文件]")
        # return "source/orig.txt", "source/orig_0.8_add.txt", "source/result.txt"
        return orig_path, siml_path, rst_path

    def openFile(self, paths):
        try:
            orig_file = open(paths[0], mode="r", encoding="utf-8")
            siml_file = open(paths[1], mode="r", encoding="utf-8")
            rst_file = open(paths[2], mode="w", encoding="utf-8")
        except IOError as e:
            print("文件打开出错，错误类型为：", e)
        print("文件打开成功！")
        return orig_file, siml_file, rst_file

    def closeFile(self, files):
        for file in files:
            file.close()
        print("文件保存成功！")

    def readFile(self, files):
        orig_str = files[0].read()
        siml_str = files[1].read()
        print("文件读取成功！")
        return orig_str, siml_str

    def writeFile(self, files, str):
        files[2].write(str)
        print("文件写入成功！")

    def calculate(self, strs):

        # 分词
        orig = jieba.lcut(strs[0])
        siml = jieba.lcut(strs[1])

        # 计算相似度
        result = Levenshtein.ratio(orig, siml)
        print("相似度计算成功！相似度为：", result)
        return str(result)

    def start(self):
        paths = self.getPath()
        files = self.openFile(paths)
        txts = self.readFile(files)
        result = self.calculate(txts)
        self.writeFile(files, result)
        self.closeFile(files)


if __name__ == "__main__":
    Main().start()
