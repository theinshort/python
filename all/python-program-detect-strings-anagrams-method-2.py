from collections import Counter
 
def is_anagram(str1, str2):
    # Create Counter objects for both strings
    counter1 = Counter(str1)
    counter2 = Counter(str2)
 
    # Compare the counters
    return counter1 == counter2
 
# Test the function
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
 
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")