# Use a list comprehension ro return a list of all the words in the following list that have more
# Cory Althoff's solution: https://github.com/calthoff/tstcs_challenge_solutions/blob/main/chap5_ex1.py

# My solution
a_list = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
new_list = [i for i in a_list if len(i) > 4]