"""
Idea: keep hashmap of letters and number of occurances - for each letter in note - 
decrease by 1 element in hash map and if one letter can't be taken - return False
O(m) + O(n) 
len(magazine) == m
len(string) == n
"""

def ransome_note(magazine, string):
    if magazine is None or string is None or len(magazine) < len(string):
        return False
    
    letters = {}
    for letter in magazine:
        if letter.isalpha():
            if not letters.has_key(letter):
                letters[letter] = 1
            else:
                letters[letter] += 1
   
    for letter in string:
        if letter.isalpha():
            if letters.has_key(letter) and letters[letter] > 0:
                letters[letter] -= 1
            else:
                return False

    return True


# test cases:
string = "no scheme"
magazine1 = "programming interviews are wierd"
magazine2 = "some text is not that good for testing ic"

print ransome_note(magazine1, string)
print ransome_note(magazine2, string) 
