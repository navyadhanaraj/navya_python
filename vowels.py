def find_vowels(input_string):
    vowels = "aeiouAEIOU"
    found_vowels = [char for char in input_string if char in vowels]
    return found_vowels
text = "My name Is Navya"
vowel_list = find_vowels(text)
print("Vowels found are:", vowel_list)
