import argparse
import re

from btree import *
from stack import *


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=None)
    parser.add_argument("-r", type=int, default=None)
    parser.add_argument("-e", type=str, default=None)
    parser.add_argument("-a", type=str, default=None)
    args = parser.parse_args()
    if args.n is not None and args.r is None:
        raise Exception("请重新输入，生成时必须输入: -r [数值范围]")

    return args


def generate():
    pass


def get_formula(path):
    dict = {}
    with open(path, "r", encoding="UTF-8") as f:
        for num, line in enumerate(f):
            dict[num] = re.match(r"[0-9]+\.\s(.*)\s?", line).group(1)
    return dict


def build_tree(formula):
    t_stack = Stack()
    curent_tree = Node()


if __name__ == "__main__":
    get_args()
