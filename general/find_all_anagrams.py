"""
Given a dictionary of words find all set of anagrams

used '/usr/share/dict/words'
"""

def find_all_anagrams():
    
    anagrams = {}
    filename = '/usr/share/dict/words'
    with open(filename, 'r') as f:
        for word in f:
            word = word.strip()
            key = ''.join(sorted(word))
            if anagrams.has_key(key):
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]


    for key in anagrams.keys():
        print "Anagrams: ", anagrams[key]
           

find_all_anagrams() 
