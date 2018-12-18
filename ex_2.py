import numpy as np
import functools

v = np.array([150, 200, 120, 175, 315, 150, 100])
m = len(v)
omega = np.array([5000, 4000, 6000])
n = len(omega)
times = np.random.random(size=[n, m])
# can be any list/tuple with length of m
# max_value <= v for each element appropriately
max_values = (1,) * m


def calc_sum(x_matrix, time_matrix):  # goal function
    return np.sum(x_matrix * time_matrix)


def rand_matrix(column_count, row_count, max_values):
    matrix = []
    for i in range(row_count):
        array = np.random.multinomial(max_values[i], np.ones(column_count) / column_count, size=1)[0]
        matrix.insert(i, array)
    return np.transpose(matrix)


def _boolean_and(bool1, bool2):
    return bool1 and bool2


def validate(sum_array):
    bool_array = sum_array < omega  # array off booleans
    return functools.reduce(_boolean_and, bool_array)


if __name__ == '__main__':
    counter = 0
    fails_count = 0
    sum = 100000000  # some big number
    min_val = sum
    min_matrix = None
    while True:
        x_matrix = rand_matrix(n, m, max_values)
        sum_array = np.sum(x_matrix * v, axis=1)
        is_valid = validate(sum_array)
        if is_valid:
            sum = calc_sum(x_matrix, times)
            if sum < min_val:
                fails_count = 0
                min_val = sum
                min_matrix = x_matrix
                print(min_val, end='\n\n')
            fails_count += 1
            if fails_count == 3000:
                break

        counter += 1
        if counter % 1000 == 0:
            print('not yet!!! {}'.format(counter))
        if counter >= 1_000_00:
            break

    print('\n\n')
    print(min_val, end='\n\n')
    print(min_matrix)
    print(counter)
