import re
import pandas as pd

def mul(a, b):
    return a * b


def read_inputs(file):
    # Read all lines as one line
    with open(file) as f:
        lines = f.read()
        return lines


def find_mul_strings(lines):
    regex_result = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
    regex_result = [element.strip("mul(").strip(")") for element in regex_result]

    mul_input = []
    for element in regex_result:
        result = [int(i) for i in element.split(",")]
        mul_input.append(result)

    return mul_input


def find_activated_mul_strings(lines):
    mul_matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", lines)
    do_matches = re.finditer(r"do\(\)", lines)
    dont_matches = re.finditer(r"don't\(\)", lines)

    mul_indices = [(match.start(), match.end()) for match in mul_matches]
    do_indices = [(match.start(), match.end()) for match in do_matches]
    dont_indices = [(match.start(), match.end()) for match in dont_matches]

    info_dicts = []
    for index in mul_indices:
        info_dicts.append({"start": index[0],
                           "end": index[1],
                           "type": "mul",
                           "function": lines[index[0]:index[1]]})

    for index in do_indices:
        info_dicts.append({"start": index[0],
                           "end": index[1],
                           "type": "do",
                           "function": None})

    for index in dont_indices:
        info_dicts.append({"start": index[0],
                           "end": index[1],
                           "type": "dont",
                           "function": None})

    info_df = pd.DataFrame(info_dicts)
    info_df = info_df.sort_values(by="start")
    info_df = info_df.reset_index(drop=True)

    # Find all indices of 'dont' and 'do'
    dont_indices = info_df.index[info_df['type'] == 'dont']
    do_indices = info_df.index[info_df['type'] == 'do']

    # Ensure each 'dont' pairs with the next 'do'
    rows_to_drop = []
    for dont_index in dont_indices:
        # Find the next 'do' after this 'dont'
        do_index = do_indices[do_indices > dont_index].min()  # First 'do' after the current 'dont'
        if not pd.isna(do_index):  # If a valid 'do' is found
            rows_to_drop.extend(range(dont_index + 1, do_index))  # Add rows to drop

    # Drop the rows
    info_df_filtered = info_df.drop(rows_to_drop)
    functions = list(info_df_filtered["function"].values)

    mul_inputs = []
    for function in functions:
        if function is not None:
            result = [int(i) for i in function.strip("mul(").strip(")").split(",")]
            mul_inputs.append(result)

    return mul_inputs


def compute(mul_input):
    result = 0
    for el in mul_input:
        result += mul(el[0], el[1])

    return result


def main():
    lines = read_inputs("inputs/day3.txt")
    # Task 1
    mul_inputs = find_mul_strings(lines)
    print(compute(mul_inputs))

    # Task 2
    activated_mul_inputs = find_activated_mul_strings(lines)
    print(compute(activated_mul_inputs))

if __name__ == "__main__":
    main()