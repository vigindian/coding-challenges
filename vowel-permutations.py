#!/usr/bin/python3

def count_vowel_permutations(n):
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        print ("range:" +str(_))
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        print (a)

    print ("=======")
    print(a)
    print(e)
    print(i)
    print(o)
    print(u)
    return (a + e + i + o + u) % (10**9 + 7)


if __name__ == '__main__':
    N = 5 
    print(count_vowel_permutations(N))
