# Coding Challenges

## 1. Count Vowel Permutations
Count all possible N-length vowel permutations that can be generated based on the given conditions. Rules:
- Each ‘a’ may only be followed by an ‘e’.
- Each ‘e’ may only be followed by an ‘a’ or an ‘i’.
- Each ‘i’ may not be followed by another ‘i’.
- Each ‘o’ may only be followed by an ‘i’ or a ‘u’.
- Each ‘u’ may only be followed by an ‘a’.

**Expected Output**:
- For input 2, output is 10 because possible combinations are "ae, ea, ei, ia, ie, io, iu, oi, ou, ua"
- For input 5, output should be 68

### 1.1. Unit Tests: Count Vowel Permutations
Unit tests embedded in the source script [vowel_permutations.py](./vowel_permutations.py)

- How to run:
```
python3 -m unittest vowel_permutations.py

#verbose-mode
python3 -m unittest -v vowel_permutations.py
```

- Sample output:
```
$ python3 -m unittest -v vowel_permutations.py 
test_vowel_permutations_float (vowel_permutations.TestVowelPermutations)
Test that vowel permutations are identified: float input ... ok
test_vowel_permutations_integer (vowel_permutations.TestVowelPermutations)
Test that vowel permutations are identified: integer input ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## 2. Find duplicate words
Find duplicate words in a string. For input, "how are you and did you eat something", output should be ['you'].

### 2.1. Unit Tests: Find duplicate words
Unit tests are in separate script [test_duplicate_words.py](./test_duplicate_words.py)

- How to run:
```
python3 -m unittest -v test_duplicate_words.py
```

- Sample output:
```
$ python3 -m unittest -v test_duplicate_words.py
test_duplicate_words_dupconsolidate (test-duplicate-words.TestDuplicateWords)
Test that duplicate words are identified and listed: consolidate duplicates ... ok
test_duplicate_words_dupone (test-duplicate-words.TestDuplicateWords)
Test that duplicate words are identified and listed: one duplicate ... ok
test_duplicate_words_empty (test-duplicate-words.TestDuplicateWords)
Test that duplicate words are identified and listed: no duplicates ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
