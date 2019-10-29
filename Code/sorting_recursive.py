#!python

from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n + m)
    TODO: Memory usage: O(n + m)"""
    merged = []
    queued = [None, None]
    items = (items1, items2)
    # Repeat until one list is empty
    while (len(items1) > 0 or queued[0] is not None) and (len(items2) > 0 or queued[1] is not None):
        # Find minimum item in both lists and append it to new list
        queued = list(map(lambda x: items[x[0]].pop(0) if x[1] is None else x[1], enumerate(queued)))
        min_index = 0 if queued[0] <= queued[1] else 1
        merged.append(queued[min_index])
        queued[min_index] = None
    # Append remaining items in non-empty list to new list
    for leftover in filter(lambda x: len(x) > 0, [queued, items1, items2]):
        merged.extend([x for x in leftover if x is not None])
    return merged


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    split = len(items) // 2
    sorted1, sorted2 = insertion_sort(items[:split]), insertion_sort(items[split:])
    return merge(sorted1, sorted2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    # print(items)
    if len(items) < 2:
        return items
    split = len(items) // 2
    sorted1, sorted2 = merge_sort(items[:split]), merge_sort(items[split:])
    return merge(sorted1, sorted2)


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
    unjumbled = split_sort_merge(jumbled)
    print(f'function(split_sort_merge): {unjumbled}')
    merge_sorted = merge_sort(jumbled)
    print(f'function(merge_sort): {merge_sorted}')