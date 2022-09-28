from argparse import ArgumentParser
from ast import operator
from fractions import Fraction  # Forbidden to delete this import!
from random import choice, randint
from re import sub, search, compile, Pattern


def get_args():
    parser = ArgumentParser()
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


def _natural_number(r: int):
    return str(randint(1, r))


def _mixed_number(r: int):
    denominator = randint(2, r)
    return (
        str(randint(1, r))
        + "'"
        + str(Fraction(randint(1, denominator - 1), denominator))
    )


def _proper_fraction(r: int):
    denominator = randint(2, r)
    return str(Fraction(randint(1, denominator - 1), denominator))


def generate(path: str, n: int, r: int):
    number_type = [_natural_number, _mixed_number, _proper_fraction]
    operator_type = [" + ", " - ", " * ", " / "]
    with open(path, "w", encoding="UTF-8") as f:
        n = n + 1
        index = 1
        while index < n:
            formula = operator = ""
            operator_number = randint(2, 4)

            for i in range(operator_number * 2 - 1):
                if i % 2 == 0:
                    formula = formula + choice(number_type)(r)
                else:
                    operator = choice(operator_type)
                    if operator == operator_type[1]:
                        m, n = search(r"\s[0-9\']$", formula).span()
                    formula = formula + operator

            formula = sub(r"\s/\s", " ÷ ", formula, 0)
            formula = sub(r"\s\*\s", " × ", formula, 0)
            f.write(str(index) + ". " + formula + " = \n")
            index = index + 1


def _get_formula(line: str, pattern: Pattern[str]):
    formula = pattern.match(line).group(1)
    formula = sub(r"÷", "/", formula, 0)
    formula = sub(r"×", "*", formula, 0)

    mixed_number_pattern = compile(r"([0-9]+)\'([0-9]+).([0-9]+)")
    mixed_numbers = mixed_number_pattern.findall(formula)
    if mixed_numbers:
        for num in mixed_numbers:
            numerator = int(num[0]) * int(num[2]) + int(num[1])
            improper_fraction = "Fraction(" + str(numerator) + "," + num[2] + ")"
            formula = mixed_number_pattern.sub(improper_fraction, formula, 1)

    proper_fraction_match = compile(r"([0-9]+)/([0-9]+)")
    proper_fraction = proper_fraction_match.findall(formula)
    if proper_fraction:
        for num in proper_fraction:
            improper_fraction = "Fraction(" + num[0] + "," + num[1] + ")"
            formula = proper_fraction_match.sub(improper_fraction, formula, 1)

    division_match = compile(r"([0-9]+)\s/\s([0-9]+)")
    division = division_match.findall(formula)
    if division:
        for num in division:
            improper_fraction = "Fraction(" + num[0] + "," + num[1] + ")"
            formula = division_match.sub(improper_fraction, formula, 1)

    return formula


def get_formula(file_path: str, equal_sign: bool = True):
    if equal_sign:
        pattern = compile(r"[0-9]+\.\s(.*)\s\=")
    else:
        pattern = compile(r"[0-9]+\.\s(.*)\s*")
    formula_dict = {}
    with open(file_path, "r", encoding="UTF-8") as f:
        for line_number, line in enumerate(f):
            formula_dict[line_number + 1] = _get_formula(line, pattern)

    return formula_dict


def get_result(formula_dict: dict):
    result_dict = {}
    for index, formula in formula_dict.items():
        result = eval(formula)
        integer_result = int(result)
        if result > 1 and integer_result != result:
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


def write_result(file_path: str, result_dict: dict):
    with open(file_path, "w", encoding="UTF-8") as f:
        for index, result in result_dict.items():
            f.write(str(index) + ". " + result + "\n")


if __name__ == "__main__":
    generate("Exercises.txt", 10000, 100)
    dict = get_formula("Exercises.txt")
    write_result("Answers.txt", get_result(dict))
    # get_difference("Exercises.txt", "Answers_wrong.txt")
    pass
