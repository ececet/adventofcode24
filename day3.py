import re

def mul(a, b):
    return a * b


def read_inputs(file):
    # Read all lines as one line
    with open(file) as f:
        lines = f.read()
        return lines

def find_mul_strings(lines):
    regex_result = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
    print(regex_result)
    regex_result = [element.strip("mul(").strip(")") for element in regex_result]
    print(regex_result)
    mul_input = []
    for element in regex_result:
        result = [int(i) for i in element.split(",")]
        mul_input.append(result)

    return mul_input


def compute(mul_input):
    result = 0
    for el in mul_input:
        result += mul(el[0], el[1])

    return result


def main():
    lines = read_inputs("inputs/day3.txt")
    mul_inputs = find_mul_strings(lines)
    print(compute(mul_inputs))


main()