def get_ordered_list_of_unique_vowels(string):
    unique_vowels = {
        vowel.lower(): None for vowel in string if vowel.lower() in "aeiou"
    }

    return unique_vowels.keys()


def vowel_printer(string):
    vowels = get_ordered_list_of_unique_vowels(string)
    print(f'Vowels: {", ".join(vowels)}')
