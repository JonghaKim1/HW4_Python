from typing import Dict, Iterable, List, Tuple, Any

def reverse_sort_dictionary(book: Dict[str, Tuple[Any, Any]]) -> List[Tuple[str, Any]]:
    #Given a dictionary mappning names (phone, age), return a list of (name, phone) tuples sorted by name in reverse order.

    if not isinstance(book, dict):
        raise TypeError("Input must be a dictionary")

    pairs: List[Tuple[str, Any]] = []
    for name, value in book.items():
        if not isinstance(name, str):
            raise TypeError("All keys must be strings (names)")
        if not isinstance(value, tuple) or len(value) < 1:
            raise TypeError("Each value must be a tuple like (phone, age)")
        phone = value[0]
        pairs.append((name, phone))

    # Reverse sort by name (descending alphabetical)
    return sorted(pairs, key=lambda t: t[0], reverse=True)