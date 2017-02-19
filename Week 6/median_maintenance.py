import heapq


def median_maintenance(integers):
    '''
    INPUT: List
    OUTPUT: List

    Keep track of the median of the numbers seen so far, given a 'streaming'
    list of numbers. Use (min-)heaps to keep track of the median. Pseudo-use
    max-heaps by negating the number. Return the resulting list of medians.
    '''
    medians = []
    # max_heap tracks the lower (smaller) half of the numbers seen thus far.
    max_heap = []
    # min_heap tracks the upper (larger) half of the numbers seen thus far.
    min_heap = []

    # First number seen is its own median. It is also added to the max_heap.
    heapq.heappush(max_heap, -integers[0])
    medians.append(-max_heap[0])

    for n in integers[1:]:
        # If the new number seen is less than the maximum number in max_heap,
        if n < -max_heap[0]:
            # Then check whether max_heap contains more numbers than min_heap.
            if len(max_heap) > len(min_heap):
                # If so, pop and push max_heap's largest number onto min_heap.
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            # Either way, push new number onto max_heap, because it's smaller.
            heapq.heappush(max_heap, -n)
        # If new number is greater than or equal to max_heap's biggest number,
        else:
            # Then check whether max_heap contains more numbers than min_heap.
            if len(max_heap) > len(min_heap):
                # If so, push the new number onto min_heap, to balance things.
                heapq.heappush(min_heap, n)
            # Otherwise (i.e., max_heap is smaller than or equal to min_heap),
            else:
                # Check if number is smaller than min_heap's smallest number.
                if n < min_heap[0]:
                    # If it is smaller, then push the new number to max_heap.
                    heapq.heappush(max_heap, -n)
                else:
                    # Elsewise, first pop min_heap's smallest number and push
                    # it onto max_heap then push the new number onto min_heap.
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
                    heapq.heappush(min_heap, n)
        # Finally, grab the median of the numbers seen thus far from max_heap.
        medians.append(-max_heap[0])
    return medians


if __name__ == '__main__':
    with open('Median.txt') as f:
        integers = [int(line) for line in f]

    medians = median_maintenance(integers)
    print('Sum Of Medians, Mod 10000:\t{}'.format(sum(medians) % 10000))
    # Answer = 1213
