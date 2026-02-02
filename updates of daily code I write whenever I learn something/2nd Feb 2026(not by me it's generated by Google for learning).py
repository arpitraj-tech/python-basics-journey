import collections

# Count vowels, consonants, digits, spaces in string
input_string = input("Enter a string to analyze: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in input_string:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")

# Find first non-repeating character
input_string_non_repeat = input("Enter a string to find the first non-repeating character: ")
char_counts = collections.Counter(input_string_non_repeat)
first_non_repeating = None
for char in input_string_non_repeat:
    if char_counts[char] == 1:
        first_non_repeating = char
        break

if first_non_repeating:
    print(f"The first non-repeating character is: {first_non_repeating}")
else:
    print("No non-repeating character found.")

# Check if two lists have common elements
list1_input = input("Enter elements for list 1 (space-separated): ").split()
list2_input = input("Enter elements for list 2 (space-separated): ").split()

set1 = set(list1_input)
has_common = False
for item in list2_input:
    if item in set1:
        has_common = True
        break

if has_common:
    print("The lists have common elements.")
else:
    print("The lists do not have common elements.")

# Rotate list by k positions
list_to_rotate_input = input("Enter elements for the list to rotate (space-separated): ").split()
k_input = int(input("Enter the number of positions to rotate: "))

k = k_input % len(list_to_rotate_input)
rotated_list = list_to_rotate_input[k:] + list_to_rotate_input[:k]
print(f"Original list: {list_to_rotate_input}")
print(f"Rotated list: {rotated_list}")

# Check palindrome without slicing
palindrome_string = input("Enter a string to check for palindrome: ")

is_palindrome = True
start = 0
end = len(palindrome_string) - 1

while start < end:
    if palindrome_string[start] != palindrome_string[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print(f"'{palindrome_string}' is a palindrome.")
else:
    print(f"'{palindrome_string}' is not a palindrome.")

# Check if two strings are anagrams using collections.Counter
string1_anagram = input("Enter the first string for anagram check: ")
string2_anagram = input("Enter the second string for anagram check: ")

if collections.Counter(string1_anagram) == collections.Counter(string2_anagram):
    print(f"'{string1_anagram}' and '{string2_anagram}' are anagrams.")
else:
    print(f"'{string1_anagram}' and '{string2_anagram}' are not anagrams.")

# Remove duplicates from list using a loop
list_with_duplicates_input = input("Enter elements for the list (space-separated) to remove duplicates: ").split()
list_without_duplicates = []
for item in list_with_duplicates_input:
    if item not in list_without_duplicates:
        list_without_duplicates.append(item)
print(f"List with duplicates removed: {list_without_duplicates}")

# Remove duplicates from a string using a loop
string_with_duplicates = input("Enter a string to remove duplicates: ")
string_without_duplicates = []
for char in string_with_duplicates:
    if char not in string_without_duplicates:
        string_without_duplicates.append(char)
print(f"String with duplicates removed: {''.join(string_without_duplicates)}")
