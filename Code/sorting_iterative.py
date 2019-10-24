#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    prev = items[0] if len(items) > 0 else None
    for index in range(1, len(items)):
        num = items[index]
        if num < prev:
            return False
        prev = num
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    while not is_sorted(items):
        for index, item in enumerate(items):
            if index < len(items) - 1 and item > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    first_unsorted_index = 0
    while not is_sorted(items):
        min_index, min_value = None, None
        for index in range(first_unsorted_index, len(items)):
            if min_value is None or items[index] < min_value:
                min_index, min_value = index, items[index]
        items[first_unsorted_index], items[min_index] = min_value, items[first_unsorted_index]
        first_unsorted_index += 1
    return items




def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Wiki says it's O(n^2) ;)
    Memory usage: O(1), only takes one extra variable to run"""
    for unsorted_index in range(1, len(items)):
        # Take first unsorted item
        unsorted = items[unsorted_index]
        # "Insert" it in sorted order in front of items
        for sorted_index in range(unsorted_index):
            if unsorted < items[sorted_index]:
                # insert the unsorted item and shift the other sorted
                # items down without adjusting the list
                held_item = unsorted
                for replace_index in range(sorted_index, unsorted_index + 1):
                    items[replace_index], held_item = held_item, items[replace_index]
                break   
    return items