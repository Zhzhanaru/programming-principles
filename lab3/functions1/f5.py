# 5.Write a function that accepts string from user 
# and print all permutations of that string.


def permutation(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permutation(a, l+1, r)
            a[l], a[i] = a[i], a[l]


s = str(input())
n = len(s)
a = list(s)
permutation(a, 0, n)