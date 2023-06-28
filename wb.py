# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)


def first_non_repeated_character(string):
    character_counts = {}
    
    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    print(character_counts)
    for char in string:
        if character_counts[char] == 1:
            return char
    print(character_counts)
    return None

print(first_non_repeated_character("test"))      
print(first_non_repeated_character("teeter"))    
print(first_non_repeated_character("trend"))     
print(first_non_repeated_character("aabbcc"))    

