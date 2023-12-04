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
    digits_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits_positions = []
    for char in line:
        if digits_numbers.count(char) != 0:
            first_index = line.find(char)
            digits_positions.append(line.find(char))

            last_index = line.rfind(char, first_index)
            if first_index != last_index:
                digits_positions.append(last_index)
    return digits_positions


def extract_digit_string_positions_in_one_line(line):
    digits_strings_one_digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits_string_positions = []
    digits_string_found = []
    for number_string in digits_strings_one_digit:
        if number_string in line:
            first_index = line.find(number_string)
            digits_string_positions.append(first_index)
            digits_string_found.append(str(digits_strings_one_digit.index(number_string) + 1))

            last_index = line.rfind(number_string, first_index)
            if first_index != last_index:
                digits_string_positions.append(last_index)
                digits_string_found.append(str(digits_strings_one_digit.index(number_string) + 1))
    return digits_string_positions, digits_string_found


def get_numbers_list(lines_list):
    numbers_list = []
    for line in lines_list:
        digit_int_positions = extract_digit_positions_in_one_line(line)
        digit_string_positions, digit_strings = extract_digit_string_positions_in_one_line(line)
        first_digit = 0
        second_digit = 0
        if len(digit_int_positions) >= 1 and len(digit_string_positions) >= 1:
            if digit_int_positions[0] > min(digit_string_positions):
                first_digit = digit_strings[digit_string_positions.index(min(digit_string_positions))]
            else:
                first_digit = line[digit_int_positions[0]]

            if digit_int_positions[len(digit_int_positions) - 1] < max(digit_string_positions):
                second_digit = digit_strings[digit_string_positions.index(max(digit_string_positions))]
            else:
                second_digit = line[digit_int_positions[len(digit_int_positions) - 1]]
        elif len(digit_int_positions) == 0 and len(digit_string_positions) > 0:
            first_digit = digit_strings[digit_string_positions.index(min(digit_string_positions))]
            second_digit = digit_strings[digit_string_positions.index(max(digit_string_positions))]
        elif len(digit_string_positions) == 0 and len(digit_int_positions) > 0:
            first_digit = line[digit_int_positions[0]]
            second_digit = line[digit_int_positions[len(digit_int_positions) - 1]]
        numbers_list.append(int(first_digit + second_digit))
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
