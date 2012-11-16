"""
given a telephone nuber print all possible words

for 7 digit number -> 3^7 numbers

O(n^3) - recursive solution
"""

keyboard = {
    '0' : ['0', '0', '0'], 
    '1' : ['1', '1', '1'],
    '2' : ['A', 'B', 'C'],
    '3' : ['D', 'E', 'F'],
    '4' : ['G', 'H', 'I'],
    '5' : ['J', 'K', 'L'],
    '6' : ['M', 'N', 'O'],
    '7' : ['P', 'R', 'S'],
    '8' : ['T', 'U', 'V'],
    '9' : ['W', 'X', 'Y'],
}

# user input is checked before
def get_char_key(telephone_key, place):
    return keyboard[telephone_key][place]


def print_t(telephone_num):
    print_telephone(telephone_num, 0, [0 for i in xrange(len(telephone_num))])


def print_telephone(telephone_num, curr_digit, result):
    if curr_digit == len(telephone_num):
        print "".join(result)
        return

    for i in xrange(3):
        # chose each letter
        result[curr_digit] = get_char_key(telephone_num[curr_digit], i)
        print_telephone(telephone_num, curr_digit + 1, result)


# iterative solution

print_t('8862665')
