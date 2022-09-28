import re


def get_formula(path):
    dict = {}
    with open(path, "r", encoding="UTF-8") as f:
        for num, line in enumerate(f):
            real_number = re.match(r"[0-9]+\.\s(.*)\s?", line).group(1)
            easy_number = re.match(r"\s?([0-9]+)\'([0-9]+)\\([0-9]+)\s?", real_number)
            
    return dict


dict = get_formula("Exercises.txt")
print(dict)
