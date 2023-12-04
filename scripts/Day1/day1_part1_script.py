def file_reading(file_name):
    with open(file_name, 'r') as file:
        lines_list = file.readlines()
        lines_list_modified = []
        for line in lines_list:
            if line.endswith('\n'):
                lines_list_modified.append(line.replace(line, line[:len(line) - 1]))
            else:
                lines_list_modified.append(line)
    return lines_list_modified


def extract_digit_positions_in_one_line(line):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits_positions = []
    for char in line:
        if digits.count(char) != 0:
            digits_positions.append(line.find(char))
    return digits_positions


def get_numbers_list(lines_list):
    numbers_list = []
    for line in lines_list:
        digit_positions = extract_digit_positions_in_one_line(line)
        number = 0
        if len(digit_positions) > 1:
            number = int(line[digit_positions[0]] + line[digit_positions[len(digit_positions) - 1]])
        elif len(digit_positions) == 1:
            number = int(line[digit_positions[0]] + line[digit_positions[0]])
        numbers_list.append(number)
    return numbers_list


def sum_all_numbers(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total


if __name__ == '__main__':
    lines_read_from_file = file_reading('input.txt')
    print(lines_read_from_file)
    print(get_numbers_list(lines_read_from_file))

    sum_of_calibration_numbers = sum_all_numbers(get_numbers_list(lines_read_from_file))
    print(f'Sum of all calibration numbers: {sum_of_calibration_numbers}')