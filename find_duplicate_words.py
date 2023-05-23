#!/usr/bin/python3

import unittest

STRING="how are you now and did you take your medicine"

def findDuplicateWords(inputString: str):
  wordArray = []
  repeatedWords = []

  #checkThis = inputString.lower().split(" ").replace(".", "")
  #checkThis = inputString.lower().split(" ")
  checkThis = inputString.replace(".", "").lower().split(" ")
  for word in checkThis:
    if word in wordArray and word not in repeatedWords:
      repeatedWords.append(word)

    wordArray.append(word)

  #print(repeatedWords)
  return repeatedWords

if __name__ == '__main__':
  duplicateWords = findDuplicateWords(STRING)
  print(duplicateWords)
