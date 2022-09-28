from argparse import ArgumentParser
from fractions import Fraction  # Forbidden to delete this import!
from random import choice, randint
from re import sub, search, compile, Pattern


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-n", type=int, default=None)
    parser.add_argument("-", type=int, default=None)
    parser.add_argument("-e", type=str, default=None)
    parser.add_argument("-a", type=str, default=None)
    args = parser.parse_args()
    if args.n is not None and args.r is None:
        raise Exception(
            "Please re-enter. You must enter like this when generating: -n [quantity] -r [value range]"
        )
    elif args.r is not None:
        generate("Exercises.txt", args.n, args.r)
        write_result("Answers.txt", get_result(get_formula("Exercises.txt")))
    if args.e is not None and args.a is not None:
        get_difference(args.e, args.a)
    else:
        raise Exception("Please re-enter and enter rightly!")
    return args


def _natural_number(r: int):
    return randint(1, r)


def _mixed_number(r: int):
    denominator = randint(2, r)
    return randint(1, r - 1) + Fraction(randint(1, denominator - 1), denominator)


def _proper_fraction(r: int):
    denominator = randint(2, r)
    return Fraction(randint(1, denominator - 1), denominator)


def _generate(r: int, operator_number: int):
    number_type = [_natural_number, _mixed_number, _proper_fraction]
    operator_type = [" + ", " - ", " * ", " / "]

    number_1 = choice(number_type)(r)
    number_2 = choice(number_type)(r)

    operator_1 = choice(operator_type)

    formula = None

    def check(formula: str, r: int, operator_number: int):
        if eval(formula) <= 0:
            return _generate(r, operator_number)
        return formula

    if operator_number == 1:
        formula = str(number_1) + operator_1 + str(number_2)
        return check(formula, r, 1)

    elif operator_number == 2:
        formula = str(number_1) + operator_1 + str(number_2)
        formula = check(formula, r, 1)

        number_1 = choice(number_type)(r)
        operator_1 = choice(operator_type)
        formula = str(number_1) + operator_1 + "(" + formula + ")"
        return check(formula, r, 2)
    elif operator_number == 3:
        formula_1 = str(number_1) + operator_1 + str(number_2)
        formula_1 = check(formula_1, r, 1)

        number_1 = choice(number_type)(r)
        number_2 = choice(number_type)(r)
        operator_1 = choice(operator_type)
        formula_2 = str(number_1) + operator_1 + str(number_2)
        formula_2 = check(formula_2, r, 1)

        operator_1 = choice(operator_type)
        formula = "(" + formula_1 + ")" + operator_1 + "(" + formula_2 + ")"
        return check(formula, r, 3)

    return formula


def generate(path: str, n: int, r: int):
    with open(path, "w", encoding="UTF-8") as f:
        formula = ""
        for index in range(1, n + 1):
            operator_number = randint(1, 3)
            formula = _generate(r, operator_number)
            proper_fraction_match = compile("([0-9]+)/([0-9]+)")
            proper_fraction = proper_fraction_match.findall(formula)
            if proper_fraction:
                for num in proper_fraction:
                    num_0 = int(num[0])
                    num_1 = int(num[1])
                    integer = num_0 // num_1
                    if integer > 1:
                        numerator = num_0 - integer * num_1
                        improper_fraction = (
                            str(integer) + "'" + str(numerator) + "div" + num[1]
                        )
                        formula = sub(
                            num[0] + "/" + num[1], improper_fraction, formula, 1
                        )
            formula = sub("div", "/", formula, 0)
            formula = sub("\s/\s", " ÷ ", formula, 0)
            formula = sub("\s\*\s", " × ", formula, 0)
            f.write(str(index) + ". " + formula + " = \n")


def _get_formula(formula: str):
    mixed_number_pattern = compile("([0-9]+)'([0-9]+).([0-9]+)")
    mixed_numbers = mixed_number_pattern.findall(formula)
    if mixed_numbers:
        for num in mixed_numbers:
            numerator = int(num[0]) * int(num[2]) + int(num[1])
            improper_fraction = "Fraction(" + str(numerator) + "," + num[2] + ")"
            formula = mixed_number_pattern.sub(improper_fraction, formula, 1)

    proper_fraction_match = compile("([0-9]+)/([0-9]+)")
    proper_fraction = proper_fraction_match.findall(formula)
    if proper_fraction:
        for num in proper_fraction:
            improper_fraction = "Fraction(" + num[0] + "," + num[1] + ")"
            formula = proper_fraction_match.sub(improper_fraction, formula, 1)

    division_match = compile("([0-9]+)\s/\s([0-9]+)")
    division = division_match.findall(formula)
    if division:
        for num in division:
            improper_fraction = "Fraction(" + num[0] + "," + num[1] + ")"
            formula = division_match.sub(improper_fraction, formula, 1)
    division_match = compile("^(.*)\s/\s(\(.*\))")
    division = division_match.findall(formula)
    if division:
        for num in division:
            improper_fraction = "Fraction(" + num[0] + "," + num[1] + ")"
            formula = division_match.sub(improper_fraction, formula, 1)

    return formula


def get_formula(file_path: str, equal_sign: bool = True):
    pattern = None
    if equal_sign:
        pattern = compile("[0-9]+\.\s(.*)\s\=")
    else:
        pattern = compile("[0-9]+\.\s(.*)\s*")
    formula_dict = {}
    with open(file_path, "r", encoding="UTF-8") as f:
        for line_number, line in enumerate(f):
            formula = pattern.match(line).group(1)
            formula = sub("÷", "/", formula, 0)
            formula = sub("×", "*", formula, 0)
            formula_dict[line_number + 1] = _get_formula(formula)

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
    # generate("Exercises.txt", 10000, 10)
    dict = get_formula("Exercises.txt")
    write_result("Answers.txt", get_result(dict))
    # get_difference("Exercises.txt", "Answers_wrong.txt")
    pass
