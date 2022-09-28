from fractions import Fraction
from random import randrange, choice
from re import sub, compile, findall, match


def _natural_number(r: int):
    return str(randrange(r))


def _mixed_number(r: int):
    denominator = randrange(r)
    return (
        str(randrange(r - 1) + 1)
        + "'"
        + str(Fraction(randrange(denominator), denominator))
    )


def _proper_fraction(r: int):
    denominator = randrange(r)
    return str(Fraction(randrange(denominator), denominator))


def generate(path: str, n: int, r: int):
    number_type = [_natural_number, _mixed_number, _proper_fraction]
    operator_type = [" + ", " - ", " * ", " / "]
    with open(path, "w", encoding="UTF-8") as f:
        for line in range(n):
            formula = ""
            operator_number = randrange(4)

            for i in range(operator_number * 2 - 1):
                if i % 2 == 0:
                    formula = formula + choice(number_type)(r)
                else:
                    formula = formula + choice(operator_type)

            f.write(str(line + 1) + ". " + formula + " = \n")


generate("Exercises.txt", 10, 10)
