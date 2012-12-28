"""
You have 2 arrays A and B. A has length n and B has length m, m << n
Find out if A contains a substring which is anagram of B

"""
def is_substring_anagram(A, B):
    if A is None or len(A) < 1:
        return False
    if B is None or len(B) < 1:
        return False
    if len(A) < len(B):
        return False

    start = 0
    end = len(B) - 1
    sorted_b = sorted(B)

    while end != len(A):
        window = sorted(A[start: end + 1])
        if window == sorted_b:
            return True
        else:
            start += 1
            end += 1
    return False

# test cases
A = ['a', 'b', 'f', 's', 'o', 'j', 'd', 'p', 'j', 'd', 'f', 's', 'p', 'f', 'j', 'p', 'o', 'p', 'o']
B1 = ['o', 'd','p','j']
B2 = ['s', 'p', 's']

print is_substring_anagram(A, B1)
print is_substring_anagram(A, B2)


