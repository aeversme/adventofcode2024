def is_array_safe(array):
    print(f'Array: {array}')
    direction = ''

    for i in range(len(array) - 1):
        # print(f'   Evaluating {array[i]} against {array[i + 1]}')
        if array[i] == array[i + 1]:
            print(f'      Values are equal')
            return False

        if i > 0:
            if array[i] > array[i + 1]:
                if direction == 'pos':
                    print(f'      Direction is neg, should be pos')
                    return False

                if abs(array[i] - array[i + 1]) > 3:
                    print(f'      Jump is too large: {abs(array[i] - array[i + 1])}')
                    return False

                direction = 'neg'

            if array[i] < array[i + 1]:
                if direction == 'neg':
                    print(f'      Direction is pos, should be neg')
                    return False

                if abs(array[i] - array[i + 1]) > 3:
                    print(f'      Jump is too large: {abs(array[i] - array[i + 1])}')
                    return False

                direction = 'pos'
        else:
            if array[i] > array[i + 1]:
                print('   Starting direction is neg')
                direction = 'neg'
            else:
                print('   Starting direction is pos')
                direction = 'pos'

            if abs(array[i] - array[i + 1]) > 3:
                print(f'      Jump is too large: {abs(array[i] - array[i + 1])}')
                return False

    return True


def is_dampened_array_safe(array):
    if not is_array_safe(array):
        print('      !! Original array is not safe')
        for i in range(len(array)):
            array_copy = array.copy()
            array_copy.pop(i)
            if is_array_safe(array_copy):
                print('         :) Found a safe dampened array\n')
                return True

        print('         !! No dampened arrays are safe\n')
        return False
    else:
        print('         :) Original array is safe\n')
        return True
