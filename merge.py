from typing import List, Iterable

def _validate_int_list(xs: Iterable) -> List[int]:
    #Return xs as a list after verifying every element is an int.
    if not isinstance(xs, list):
        raise TypeError("input must be a list")
    for x in xs:
        if not isinstance(x, int):
            raise TypeError("All elements must be integers")
    return xs

def _merge_sorted(a: List[int], b: List[int]) -> List[int]:
    #Merge two sorted lists into one sorted ascending list
    i = j = 0
    out: List[int] = []
    len_a, len_b = len(a), len(b)

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1

    #One of them may have leftovers
    if i < len_a:
        out.extend(a[i:])
    if j < len_b:
        out.extend(b[j:])
    return out

def _mergesort(xs: List[int]) -> List[int]:
    n = len(xs)
    if n <= 1:
        return xs[:]
    
    mid = n // 2
    left = _mergesort(xs[:mid])
    right = _mergesort(xs[mid:])
    return _merge_sorted(left, right)

def merge_list(list1: List[int], list2: List[int]) -> List[int]:
    a = _validate_int_list(list1)
    b = _validate_int_list(list2)

    combine = a + b
    return _mergesort(combine)
