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
'''
In Python, the % symbol is the Modulo operator, and it gives you the Remainder of a division.
​It is not "mode" (which is a statistics term for the most frequent number).
​Using your example: "Python" (k=2)
​The string "Python" has 6 letters. When you run k = 2 % 6, Python does the following math:
​Divide: 2 \div 6 = 0
​Calculate what's left over: Since 6 goes into 2 zero times, the entire 2 is left over.
​Result: The remainder is 2.
​So, k remains 2.
​Why use the Remainder logic?
​The "Remainder" trick is used to "wrap around" numbers. Look at what happens if k is larger than the string length:
​If k = 6: 6 \div 6 = 1 with 0 remainder. (k=0) \rightarrow No rotation.
​If k = 7: 7 \div 6 = 1 with 1 remainder. (k=1) \rightarrow Rotates by 1.
​If k = 8: 8 \div 6 = 1 with 2 remainder. (k=2) \rightarrow Rotates by 2.
​Summary: The % sign ensures that no matter how big the number the user types in, it will always be converted into a valid "remainder" that fits inside the length of your list or string
In Python, 2 % 6 will give you 2.
​Here is why:
​The Operator: The % symbol is the modulo operator, which calculates the remainder after division.
​The Math: * You are trying to divide 2 by 6.
​6 goes into 2 zero times (2 // 6 = 0).
​Since it went in zero times, the entire 2 is left over.
​The Result: Because 2 is the "leftover" part, the remainder is 2.
​Simple Rule of Thumb:
​Whenever the first number is smaller than the second number (like 2 < 6), the result of the modulo will always be the first number itself.
​1 % 6 = 1
​2 % 6 = 2
​5 % 6 = 5
​6 % 6 = 0 (Because 6 goes into 6 perfectly with nothing left over)
In integer math (like Python's % operator), the remainder is always a whole number, not a decimal.
​When you divide 2 by 6:
​Quotient: 6 goes into 2 0 times.
​Product: 0 \times 6 = 0.
​Remainder: 2 - 0 = \mathbf{2}.
​The "0.333..." result you are thinking of is the decimal quotient, which happens only if you continue the division into fractions. In coding, the modulo operator stops once it finds the leftover whole number.
'''

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

"""
CodeChef: The Lead Game (TLG) Solution
Problem Statement: The problem asks us to simulate a game played between two players, Player 1 and Player 2. In each round, both players score a certain number of points. We need to find the maximum lead obtained by any player at the end of any round and declare the player who had this maximum lead as the winner.

Approach:

Initialize score1, score2, max_lead, and winner to 0. max_lead will store the largest lead found so far, and winner will store the player (1 or 2) who achieved that lead.
Iterate through each round of the game.
In each round, read the scores of Player 1 and Player 2 for that round.
Add these scores to their respective total scores (score1 and score2).
Calculate the current lead for Player 1 over Player 2 (lead1 = score1 - score2).
Calculate the current lead for Player 2 over Player 1 (lead2 = score2 - score1).
Compare lead1 and lead2 to find the absolute lead in this round.
If the current absolute lead is greater than max_lead, update max_lead and set the winner to the player who currently has the lead.
After all rounds, print the winner and max_lead.
"""
# cook your dish here
T = int(input())

score1 = 0
score2 = 0
max_lead = 0
winner = 0

for _ in range(T):
    s1, s2 = map(int, input().split())
    score1 += s1
    score2 += s2

    current_lead = abs(score1 - score2)

    if current_lead > max_lead:
        max_lead = current_lead
        if score1 > score2:
            winner = 1
        else:
            winner = 2

print(winner, max_lead)

"""above was also by Google not solved by me"""
