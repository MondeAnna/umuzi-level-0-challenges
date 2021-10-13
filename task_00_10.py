def print_common_chars(string_one, string_two):
    set_one = set(string_one)
    set_two = set(string_two)

    intersection = set_one.intersection(set_two)
    common_letters = ', '.join(intersection)

    print(f'Common letters: {common_letters}')
