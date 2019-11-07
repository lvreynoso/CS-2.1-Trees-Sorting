#!python

from sorting_iterative import insertion_sort
import random

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
    Running time: O(n^2)
    Memory usage: O(n)"""
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
    `[low...high]` by choosing a pivot (randomly selected) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n)
    Memory usage: O(n)"""
    # Choose a pivot via random integer within the range
    pivot_index = random.randint(low, high)
    pivot = items[pivot_index]
    lows, highs = [], []
    # Loop through all items in range [low...high]
    for index in range(low, high + 1):
        if index == pivot_index:
            continue
        item = items[index]
        # Move items less than pivot into front of range [low...p-1]
        if item <= pivot:
            lows.append(item)
        # Move items greater than pivot into back of range [p+1...high]
        else:
            highs.append(item)
    # Move pivot item into final position [p] and return index p
    pivot_index = low + len(lows)
    items[low:pivot_index] = lows if len(lows) > 0 else items[low:pivot_index]
    items[pivot_index] = pivot
    items[pivot_index + 1:high + 1] = highs if len(highs) > 0 else items[pivot_index + 1:high + 1]
    return pivot_index



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n log n)
    Worst case running time: O(n^2) (though extremely unlikely thanks to random pivot)
    Memory usage: O(n)"""
    # Check if high and low range bounds have default values (not given)
    low = 0 if low is None else low
    high = len(items) - 1 if high is None else high
    # Check if list or range is so small it's already sorted (base case)
    if low >= high:
        return items
    # Partition items in-place around a pivot and get index of pivot
    pivot_index = partition(items, low, high)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot_index - 1)
    quick_sort(items, pivot_index + 1, high)
    return items


if __name__ == '__main__':
    # first, second = [0, 1, 3, 5, 7, 9, 11], [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    # combined = merge(first, second)
    # print(f'function(merge): {combined}')
    jumbled = [17, 73, 14, 10, 36, 75, 25, 39, 55, 4, 35, 54, 22, 7, 54, 13, 17, 84, 41, 91]
    # unjumbled = merge_sort(jumbled)
    # print(f'function(merge_sort): {unjumbled}')
    # dwarves = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    # undwarves = merge_sort(dwarves)
    # print(f'function(merge_sort): {undwarves}')
    # print(dwarves)
    quick_sort(jumbled)
    print(jumbled)