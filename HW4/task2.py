def print_dict(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if type(value) not in [int, float, bool, str, tuple, frozenset]:
            value = str(value)
        new_dict[value] = key

    return new_dict


print(print_dict(a=1, b=[123], c='wrw'))
