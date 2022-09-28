from argparse import ArgumentParser
from fractions import Fraction
import math  # Forbidden to delete this import!
from random import choice, randint
from re import sub, compile


def _natural_number(r: int):
    return randint(1, r)


def _mixed_number(r: int):
    denominator = randint(2, r)
    return randint(1, r - 1) + Fraction(randint(1, denominator - 1), denominator)


def _proper_fraction(r: int):
    denominator = randint(2, r)
    return Fraction(randint(1, denominator - 1), denominator)


def check(formula: str, r: int, operator_number: int):
    a = eval(formula)
    if math.isclose(a, 0, rel_tol=1e-6):
        return _generate(r, operator_number)
    return formula


def _generate(r: int, operator_number: int):
    number_type = [_natural_number, _mixed_number, _proper_fraction]
    operator_type = [" + ", " - ", " * ", " / "]

    number_1 = choice(number_type)(r)
    number_2 = choice(number_type)(r)

    operator_1 = choice(operator_type)

    formula = None

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


a = check("1/6 - (1 / 3/4)", 10, 2)

print(a)
