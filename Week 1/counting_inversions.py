def counting_inversions(A):
    '''
    INPUT: Array
    OUTPUT: Array, Int

    Sort the given array, using the divide-and-conquer approach. Return the
    sorted array, as well as the number of inversions needed to sort the array.
    '''
    n = len(A)
    if n < 2:
        return A, 0
    m = int(n / 2)
    L, x = counting_inversions(A[:m])
    R, y = counting_inversions(A[m:])
    A, z = counting_split_inversions(L, R)
    return A, x + y + z


def counting_split_inversions(L, R):
    '''
    INPUT: Array, Array
    OUTPUT: Array, Int

    Combine and sort the 2 given arrays into 1 array. Return the sorted array,
    as well as the number of inversions needed to combine and sort the arrays.
    '''
    n1 = len(L)
    n2 = len(R)
    n = n1 + n2
    A = []
    c, i, j = 0, 0, 0
    for k in range(n):
        if i < n1 and (j >= n2 or L[i] <= R[j]):
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1
            c += n1 - i
    return A, c


if __name__ == '__main__':
    with open('IntegerArray.txt') as f:
        integers = [int(line) for line in f]
    print('# Integers:\t{}'.format(len(integers)))

    integers, count = counting_inversions(integers)
    print('# Inversions:\t{}'.format(count))
    # Answer: 2407905288
