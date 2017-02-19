from collections import Counter


def two_sum(numbers, integers):
    '''
    INPUT: List, Counter
    OUTPUT: Int

    Return the number of 2-Sum numbers, i.e., the number of numbers from the
    given list that can be found by summing 2 numbers from the given Counter.
    '''
    count = 0
    for number in numbers:
        if not number % 100:
            print(number)
        for integer in integers:
            if ((number - integer) in integers) and \
                    (integer != (number - integer) or integers[integer] > 1):
                count += 1
                break
    return count


if __name__ == '__main__':
    integers = Counter()
    with open('2sum.txt') as f:
        for line in f:
            integers[int(line)] += 1

    numbers = range(-10000, 10001)
    count = two_sum(numbers, integers)
    print('\nNumber Of 2-Sum Numbers:\t{}'.format(count))
    # Answer = 427
