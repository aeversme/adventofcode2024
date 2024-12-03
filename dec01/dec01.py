from input_handler import convert_input


def main():
    with open('data.txt') as i:
        i_raw = i.readlines()

    data = convert_input(i_raw)

    list1 = []
    list2 = []

    for line in data:
        line_split = line.split(' ')
        # print(line_split)
        list1.append(line_split[0])
        list2.append(line_split[-1])

    total = 0
    part = 2

    if part == 1:
        print('Processing part 1')
        list1.sort()
        list2.sort()

        for i in range(len(list1)):
            difference = abs(int(list1[i]) - int(list2[i]))
            print(f'{list1[i]} & {list2[i]}: difference is {difference}')
            total += difference
    else:
        print('Processing part 2')
        count_dict = {}
        list2_set = set(list2)

        for n in list2_set:
            count_dict[n] = list2.count(n)

        print(count_dict)

        for i in range(len(list1)):
            try:
                total += int(list1[i]) * count_dict[list1[i]]
            except KeyError:
                print(f'Number {list1[i]} not found in list2')

    return total


result = main()
print(f'\nResult is: {result}')
