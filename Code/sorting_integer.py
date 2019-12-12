#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    minimum, maximum = min(numbers), max(numbers)
    # TODO: Create list of counts with a slot for each number in input range
    counts = [0 for _ in range(minimum, maximum + 1)]
    # TODO: Loop over given numbers and increment each number's count
    for number in numbers:
        counts[number - minimum] += 1
    # TODO: Loop over counts and append that many numbers into output list
    # output = []
    # for number, count in enumerate(counts):
    #     output.extend([number + minimum for _ in range(count)])
    # return output
    # FIXME: Improve this to mutate input instead of creating new output list
    index = 0
    for number, count in enumerate(counts):
        numbers[index:index + count] = [number + minimum] * count
        index += count
    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

def test_integer_sort():
    jumbled = [17, 73, 14, 10, 36, 75, 25, 39, 55, 4, 35, 54, 22, 7, 54, 13, 17, 84, 41, 91]
    print(f'Sorting {jumbled}')
    unjumbled = counting_sort(jumbled)
    print(f'Result: {unjumbled}')
    is_sorted = unjumbled == sorted(jumbled)
    print(is_sorted)


if __name__ == '__main__':
    test_integer_sort()