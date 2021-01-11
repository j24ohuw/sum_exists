def sum_exists(arr, const):
    my_set = set()
    while arr:
        val = arr.pop()
        if type(val) != int:
            raise ValueError
        if val in my_set:
            return True
        my_set.add(const - val)
    return False
