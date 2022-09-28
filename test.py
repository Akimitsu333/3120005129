import re
from fractions import Fraction


def get_formula(file_path: str):
    formula_dict = {}
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

            formula_dict[line_number] = formula

    return formula_dict


resault_dict = get_formula("Exercises.txt")
for key, formula in resault_dict.items():
    print(eval(formula))
