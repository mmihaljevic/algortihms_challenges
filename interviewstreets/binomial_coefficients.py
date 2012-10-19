#!/usr/local/bin/python

"""
Solution to interviewsstreet challenge:
https://www.interviewstreet.com/challenges/dashboard/#problem/4fe19c4f35a0e


"""


def bin_coefficients(n, p):
    mod, ndiv = n, 1
    while mod > 0:
        ndiv = ndiv * ((mod % p) + 1)
        mod = mod / p
    return (n + 1 - ndiv)

test_cases = int(raw_input())

for i in xrange(test_cases):
    N, P = raw_input().split()
    n = int(N)
    p = int(P)
    print bin_coefficients(n,p)
