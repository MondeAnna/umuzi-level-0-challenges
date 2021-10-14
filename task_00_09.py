from collections import Counter


def vowel_printer(string):
    vowels = Counter()
    vowels.update(vowel.lower() for vowel in string if vowel.lower() in "aeiou")
    vowels_str = ", ".join(vowels)
    print(f"Vowels: {vowels_str}")
