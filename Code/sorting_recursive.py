#!python

from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m)
    Memory usage: O(n + m)"""
    merged = []
    iterators = (iter(items1), iter(items2))
    queued = [next(iterators[0]), next(iterators[1])]
    # Repeat until one list is empty
    while True:
        # Find minimum item in both lists and append it to new list
        min_index = int(queued[1] <= queued[0])
        merged.append(queued[min_index])
        try:
            queued[min_index] = next(iterators[min_index])
        except StopIteration:
            # Append remaining items in non-empty list to new list
            leftover_index = int(not min_index)
            merged.append(queued[leftover_index])
            merged.extend(list(iterators[leftover_index]))
            break
    return merged

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    split = len(items) // 2
    # Sort each half using any other sorting algorithm
    sorted1, sorted2 = insertion_sort(items[:split]), insertion_sort(items[split:])
    # Merge sorted halves into one list in sorted order
    for index, item in enumerate(merge(sorted1, sorted2)):
        items[index] = item
    return items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n) since we're constantly splitting things into 2 parts
    Memory usage: O(n log n) since we're doing a lot of duplication of items"""
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items
    # Split items list into approximately equal halves
    split = len(items) // 2
    # Sort each half by recursively calling merge sort
    sorted1, sorted2 = merge_sort(items[:split]), merge_sort(items[split:])
    # Merge sorted halves into one list in sorted order
    items[:] = merge(sorted1, sorted2)
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == '__main__':
    first, second = [0, 1, 3, 5, 7, 9, 11], [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    combined = merge(first, second)
    print(f'function(merge): {combined}')
    jumbled = [17, 73, 14, 10, 36, 75, 25, 39, 55, 4, 35, 54, 22, 7, 54, 13, 17, 84, 41, 91]
    unjumbled = merge_sort(jumbled)
    print(f'function(merge_sort): {unjumbled}')
    dwarves = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    undwarves = merge_sort(dwarves)
    print(f'function(merge_sort): {undwarves}')
    print(dwarves)