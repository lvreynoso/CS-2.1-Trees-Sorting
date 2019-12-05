#!python

from binaryheap import BinaryMinHeap

# not ideal for an in-place heap_sort, but works
# it's all about that immutability anyway amirite? # this comment brought to you by FUNCTIONAL PROGRAMMING (FP) GANG
def heap_sort(items):
    heap = BinaryMinHeap(items)
    for index, mass in enumerate(heap):
        items[index] = mass
    return items

def test_heap_sort():
    jumbled = [17, 73, 14, 10, 36, 75, 25, 39, 55, 4, 35, 54, 22, 7, 54, 13, 17, 84, 41, 91]
    print(f'Sorting {jumbled}')
    unjumbled = heap_sort(jumbled)
    print(f'Result: {unjumbled}')
    is_sorted = unjumbled == sorted(jumbled)
    print(is_sorted)


if __name__ == '__main__':
    test_heap_sort()