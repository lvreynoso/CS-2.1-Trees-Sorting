#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n), always
    Memory usage: O(1) since it's a constant size no matter the input"""
    # Check that all adjacent items are in order, return early if so
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
    Running time: O(n^2) roughly
    Memory usage: O(1) since items are merely swapped"""
    # Repeat until all items are in sorted order
    while not is_sorted(items):
        for index, item in enumerate(items):
            # Swap adjacent items that are out of order
            if index < len(items) - 1 and item > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) cause we make n comparisons n times?
    Memory usage: O(1) since we're just swapping stuff around"""
    for unsorted_index in range(len(items)):
        min_index, min_value = None, None
        # Find minimum item in unsorted items
        for index in range(unsorted_index, len(items)):
            if min_value is None or items[index] < min_value:
                min_index, min_value = index, items[index]
        # Swap it with first unsorted item
        items[unsorted_index], items[min_index] = min_value, items[unsorted_index]
    return items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Wiki says it's O(n^2) ;)
    Memory usage: O(1), only takes one extra variable to run"""
    for unsorted_index in range(1, len(items)):
        # Take first unsorted item
        unsorted = items[unsorted_index]
        # Find the location it belongs in the sorted items
        target_index = unsorted_index
        while unsorted < items[target_index-1] and target_index > 0:
            target_index -= 1
        # insert the unsorted item and shift the other sorted
        # items down without adjusting the list
        held_item = unsorted
        for replace_index in range(target_index, unsorted_index + 1):
            items[replace_index], held_item = held_item, items[replace_index] 
    return items