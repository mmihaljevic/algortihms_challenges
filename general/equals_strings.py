"""
Given 2 strings S1 & S2, S1 contains A-Z, and S2 cointains A-Z, *, ?
* - any character 0 of any number of times
? - any character 0 or one number of times

is S1 == S2
"""

def is_equal(S1, S2):
    if S1 is None or len(S1) < 1:
        return False
    if S2 is None or len(S2) < 1:
        return False

    i = 0
    j = 0
    l1 = len(S1) -1
    l2 = len(S2) -1

    while i <= l1 and j <= l2:
        if S2[j] == '?':
            # no matching?
            if j+1 <= l2 and S1[i] == S2[j+1]:
                # move only S2 pointer
                j += 1
            else:
                #move both pointers like it was one matching
                i += 1
                j += 1
        elif S2[j] == '*':
            # no matching?
            if j+1 <= l2 and S1[i] == S2[j+1]:
                j += 1
            else:
                # move first pointer because it can be more to match
                i += 1
        else:
            if S1[i] == S2[j]:
                i += 1
                j += 1
            else:
                return False

    # went trough both string
    if i == len(S1) and j == len(S2):
        return True
    else:
        return False

# test cases:
S1a = "ABC"
S2a = "ABD"

print is_equal(S1a, S2a)

S1b = "ABCDEFGABCD"
S2b = "ABCDEFGABCD"

print is_equal(S1b, S2b)

# zero ocurances
S1c = "ABCDFGABFC"
S2c = "ABCD*FGABFC"

print is_equal(S1c, S2c)

# more than one occurance
S1d = "ABCDEFMMNGABFC"
S2d = "ABCDEF*GABFC"

print is_equal(S1d, S2d)

# zero ocurance
S1e = "ABCDEFGABCDEFG"
S2e = "ABCDE?FGABCDEFG"

print is_equal(S1e, S2e)

# one occurance
S1f = "ABCDEFGABCDEFG"
S2f = "ABCDE?GABCDEFG"

print is_equal(S1f, S2f)
