def quicksort(A, l, r, z):
    '''
    INPUT: Array, Int, Int, Int
    OUTPUT: Array, Int

    Sort the given array, using Quicksort. The first 2 given integers
    corespond to the index position of the left and right elements,
    respectively. The 3rd given integer determines which pivot to use.
    Return the sorted array, and the number of comparisons required.
    '''
    count_l, count_r = 0, 0
    if l < r:
        (A, p) = partition(A, l, r, z)
        (A, count_l) = quicksort(A, l, p - 1, z)
        (A, count_r) = quicksort(A, p + 1, r, z)
    return A, (max(r - l, 0) + count_l + count_r)


def partition(A, l, r, z):
    '''
    INPUT: Array, Int, Int, Int
    OUTPUT: Array, Int

    Move all elements that are less than the pivot to the left of the pivot.
    Return the array and the final index position of the pivot in the array.
    '''
    A, p = choose_pivot(A, l, r, z)
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < p:
            A = swap(A, i, j)
            i += 1
    A = swap(A, l, i - 1)
    return A, i - 1


def choose_pivot(A, l, r, z):
    '''
    INPUT: Array, Int, Int, Int
    OUTPUT: Array, Int

    Choose the pivot around which to sort the given array. The pivot may be:
    - The left element
    - The right element
    - The median element
    Swap the chosen pivot with the left element. Return the array and pivot.
    '''
    if z == 1:
        q = l
    elif z == 2:
        q = r
    else:
        m = int((l + r) / 2)
        T = [(l, A[l]), (m, A[m]), (r, A[r])]
        q = sorted(T, key=lambda x: x[1])[1][0]
    A = swap(A, l, q)
    return A, A[l]


def swap(A, i, j):
    '''
    INPUT: Array, Int, Int
    OUTPUT: Array

    Given an array and 2 index positions, swap the 2 elements corresponding to
    the given index positions. Return the new array with the swapped elements.
    '''
    A[i], A[j] = A[j], A[i]
    return A


if __name__ == '__main__':
    with open('QuickSort.txt') as f:
        integers = [int(line) for line in f]
    print('# Integers:\t{}'.format(len(integers)))

    # Question 1
    (integers1, count1) = quicksort(integers[:], 0, len(integers) - 1, 1)
    print('# Comparisons:\t{}\t(Left Pivot)'.format(count1))
    # Answer: 162085

    # Question 2
    (integers2, count2) = quicksort(integers[:], 0, len(integers) - 1, 2)
    print('# Comparisons:\t{}\t(Right Pivot)'.format(count2))
    # Answer: 164123

    # Question 3
    (integers3, count3) = quicksort(integers[:], 0, len(integers) - 1, 3)
    print('# Comparisons:\t{}\t(Median Pivot)'.format(count3))
    # Answer: 138382
