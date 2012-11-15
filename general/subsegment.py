"""
solution to subsegmenting problem
Questions to ask interviewer:
1. what if the input string is already a word?
2. should I only consider segmentation into two words? - look at first solution
3. what if input string cannot be segmented?
4. what about spelling correction?
5. what if there are multiple valid segmentations?
6. what operations does dictionary support?
7. how big is the dictionary?

"""

dictionary = {}

def initialize_dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        for word in f:
            word = word.strip()
            if len(word) > 0 and not dictionary.has_key(word):
                dictionary[word] = None

# simplest solution - segmentation only into two words
def subsegment_simple(string):
    if string is None or len(string) < 1:
        return False
    # situation when the input string is already a word
    if dictionary.has_key(string):
        return string 
    for i in xrange(len(string)):
        prefix = string[: i+1]
        if dictionary.has_key(prefix):
            sufix = string[i+1 :]
            if dictionary.has_key(sufix):
                return prefix + " " + sufix

    return False

# general solution - recursive O(2^n)
def subsegment_general(string):
    if string is None or len(string) < 1:
        return None
    # stop when sting is a word
    if dictionary.has_key(string):
        return string

    # iterate 
    for i in xrange(len(string)):
        prefix = string[ : i+1]
        if dictionary.has_key(prefix):
            sufix = string[i+1 :]
            sub_sufix = subsegment_general(sufix)
            if sub_sufix != None:
                return prefix + " " + sub_sufix 
    


initialize_dictionary()
print subsegment_simple('peanutbutter')
print subsegment_general('peanutbutter')
