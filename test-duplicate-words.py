#!/usr/bin/python3

import unittest

from find_duplicate_words import findDuplicateWords

class TestDuplicateWords(unittest.TestCase):
  def test_duplicate_words_empty(self):
    """
    Test that duplicate words are identified and listed: no duplicates
    """
    inputString = "how are you"
    result = findDuplicateWords(inputString)
    self.assertEqual(result, [])

  def test_duplicate_words_dupone(self):
    """
    Test that duplicate words are identified and listed: one duplicate
    """
    inputString = "how are you now and did you take your medicine"
    result = findDuplicateWords(inputString)
    self.assertEqual(result, ['you'])

  def test_duplicate_words_dupconsolidate(self):
    """
    Test that duplicate words are identified and listed: consolidate duplicates
    """
    inputString = "how are you now and how did you take your medicine now. It will be helpful if you could answer me now. Thanks."
    result = findDuplicateWords(inputString)
    self.assertEqual(result, ['how', 'you', 'now'])

if __name__ == '__main__':
  unittest.main(verbosity=2)
