from input_handler import convert_input
from array_handler import is_array_safe, is_dampened_array_safe


def main():
    with open('data.txt') as i:
        i_raw = i.readlines()

    data = convert_input(i_raw)
    conv_data = []

    for line in data:
        line_split = line.split(' ')
        for i in range(len(line_split)):
            line_split[i] = int(line_split[i])
        print(line_split)
        conv_data.append(line_split)

    total = 0
    part = 2

    if part == 1:
        print('Processing part 1\n')

        for array in conv_data:
            if is_array_safe(array):
                print('   Array is safe')
                total += 1
            else:
                print(f'      Array is not safe')
    else:
        print('Processing part 2\n')

        for array in conv_data:
            if is_dampened_array_safe(array):
                total += 1

    return total


result = main()
print(f'\nResult is: {result}')
