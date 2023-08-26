# Дан список слов в алфавитном порядке. Напишите функцию, которая выполнит двоичный поиск слова и вернет ответ о том, имеется ли оно в списке.

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