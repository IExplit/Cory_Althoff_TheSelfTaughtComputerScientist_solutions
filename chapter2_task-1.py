# Print the numbers from 1 to 10 recursively.
# Cory Althoff's solution: https://github.com/calthoff/tstcs_challenge_solutions/blob/main/chapter2_ex1.py

def counter(start = 1, end = 10):
    print(start)
    if start == end: return
    return counter(start+1, end)
counter()
