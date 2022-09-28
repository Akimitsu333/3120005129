import re
import argparse
from random import randrange
from fractions import Fraction  # Forbidden to delete this import!


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=None)
    parser.add_argument("-r", type=int, default=None)
    parser.add_argument("-e", type=str, default=None)
    parser.add_argument("-a", type=str, default=None)
    args = parser.parse_args()
    if args.n is not None and args.r is None:
        raise Exception(
            "Please re-enter. You must enter like this when generating: -n [quantity] -r [value range]"
        )

    return args


def generate(n: int, r: int):

    pass


def _get_formula(file_path: str, pattern: re.Pattern[str]):
    formula_dict = {}
    with open(file_path, "r", encoding="UTF-8") as f:
        for line_number, line in enumerate(f):
            formula_origin = pattern.match(line).group(1)
            formula = re.sub(r"÷", "/", formula_origin, 0)

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

            formula_dict[line_number + 1] = formula

    return formula_dict


def get_formula(file_path: str, equal_sign: bool = True):
    if equal_sign:
        pattern = re.compile(r"[0-9]+\.\s(.*)\s\=")
    else:
        pattern = re.compile(r"[0-9]+\.\s(.*)\s*")

    return _get_formula(file_path, pattern)


def get_result(formula_dict: dict):
    result_dict = {}
    for index, formula in formula_dict.items():
        result = eval(formula)
        integer_result = int(result)
        if integer_result != result:
            result = str(integer_result) + "'" + str(result - integer_result)
        else:
            result = str(result)
        result_dict[index] = result

    return result_dict


def get_difference(exercises_path: str, answers_path: str):
    correct_index = set()
    wrong_index = set()
    exercises_result_dict = get_result(get_formula(exercises_path))
    answers_result_dict = get_result(get_formula(answers_path, False))

    for index, result in answers_result_dict.items():
        if result == exercises_result_dict.get(index):
            correct_index.add(index)
        else:
            wrong_index.add(index)

    with open("Grade.txt", "w", encoding="UTF-8") as f:
        f.write(
            "Correct: "
            + str(len(correct_index))
            + " ( "
            + str(correct_index)[1:-1]
            + " )"
            + "\n"
        )
        f.write(
            "Wrong: " + str(len(wrong_index)) + " ( " + str(wrong_index)[1:-1] + " )"
        )


def switch_func():
    pass


if __name__ == "__main__":
    dict = get_formula("Exercises.txt")
    result = get_result(dict)
    print(result)
    get_difference("Exercises.txt", "Answers_wrong.txt")
    pass
