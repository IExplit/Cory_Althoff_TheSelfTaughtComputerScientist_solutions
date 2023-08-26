# Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list.
# Cory Althoff's solution (Does not work): https://github.com/calthoff/tstcs_challenge_solutions/blob/main/chapter3_ex1.py

# My solution
def binary_search1(an_iterable, word):
    first = 0
    last = len(an_iterable) - 1
    while last >= first:
        mid = (first + last) // 2
        for i in range(len(word)):
            if ord(an_iterable[mid][i]) > ord(word[i]):
                last = mid - 1
                break
            elif ord(an_iterable[mid][i]) < ord(word[i]):
                first = mid + 1
                break
            elif i == len(an_iterable[mid]) - 1:
                if len(word) == len(an_iterable[mid]):
                    return True
                elif len(word) < len(an_iterable[mid]):
                    last = mid - 1
                    break
                elif len(word) > len(an_iterable[mid]):
                    first = mid + 1
                    break
    return False
