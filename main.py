import argparse
import re
from fractions import Fraction


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


def get_formula(file_path, callback_func):
    resault_dict = {}
    with open(file_path, "r", encoding="UTF-8") as f:
        for line_number, line in enumerate(f):
            formula = re.match(r"[0-9]+\.\s(.*)\s?", line).group(1)

            mixed_number_pattern = re.compile(r"([0-9]+)\'([0-9]+).([0-9]+)")
            mixed_numbers = mixed_number_pattern.findall(formula)
            if mixed_numbers:
                for num in mixed_numbers:
                    numerator = int(num[0]) * int(num[2]) + int(num[1])
                    improper_fraction = (
                        "Fraction(" + str(numerator) + "," + num[2] + ")"
                    )
                    formula = mixed_number_pattern.sub(improper_fraction, formula, 1)

            proper_fraction_match = re.compile(r"([0-9]+)/([0-9]+)")
            proper_fraction = proper_fraction_match.findall(formula)
            if proper_fraction:
                for num in proper_fraction:
                    improper_fraction = "Fraction(" + num[0] + "," + num[1] + ")"
                    formula = proper_fraction_match.sub(improper_fraction, formula, 1)

            # number = re.sub(
            #     r"[0-9]+\'[0-9]+/[0-9]+",
            #     numerator + "/" + number_3,
            #     real_number,
            # )
            # resault_dict[num] = number
            resault_dict[line_number] = formula

    return resault_dict


def caculate(formula):
    result = eval(formula)


if __name__ == "__main__":
    get_args()
