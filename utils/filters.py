def filter_items(items, filter_func):
    """Filter items based on a filter function."""
    return [item for item in items if filter_func(item)]

def sort_items(items, key_func, reverse=False):
    """Sort items based on a key function."""
    return sorted(items, key=key_func, reverse=reverse)