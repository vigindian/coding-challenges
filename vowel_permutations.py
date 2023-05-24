#!/usr/bin/python3

# Count all possible N-length vowel permutations that can be generated based on the given conditions. Rules:
#    Each ‘a’ may only be followed by an ‘e’.
#    Each ‘e’ may only be followed by an ‘a’ or an ‘i’.
#    Each ‘i’ may not be followed by another ‘i’.
#    Each ‘o’ may only be followed by an ‘i’ or a ‘u’.
#    Each ‘u’ may only be followed by an ‘a’.

import unittest

def count_vowel_permutations(n: int):
    n = int(n)
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

    return (a + e + i + o + u) % (10**9 + 7)

class TestVowelPermutations(unittest.TestCase):
  def test_vowel_permutations_integer(self):
    """
    Test that vowel permutations are calculated: integer input
    """
    N = 5
    result = count_vowel_permutations(N)
    self.assertEqual(result, 68)

  def test_vowel_permutations_float(self):
    """
    Test that vowel permutations are calculated: float input
    """
    N = 6.0
    result = count_vowel_permutations(N)
    self.assertEqual(result, 129)

  def test_vowel_permutations_string(self):
    """
    Test expected error for vowel permutations calculation: string
    """
    N = "invalid_input"
    with self.assertRaises(ValueError):
      result = count_vowel_permutations(N)


if __name__ == '__main__':
    N = 2
    print(count_vowel_permutations(N))
