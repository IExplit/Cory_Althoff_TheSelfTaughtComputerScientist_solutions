# Print the numbers from 1 to 10 recursively.


def counter(start = 1, end = 10):
    print(start)
    if start == end: return
    return counter(start+1, end)
counter()
