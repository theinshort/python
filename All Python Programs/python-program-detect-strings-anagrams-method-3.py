def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
 
    if len(str1) == 1:
        return str1 == str2
 
    for i in range(len(str1)):
        if str1[i] in str2:
            remaining_chars = str2[:str2.index(str1[i])] + str2[str2.index(str1[i]) + 1:]
            if is_anagram(str1[:i] + str1[i+1:], remaining_chars):
                return True
 
    return False
 
# Test the function
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
 
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")