def get_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(a_list, start, end):
    for i in range(start+1, end+1):
        num = i
        if i < len(a_list):
            while a_list[i-1] > a_list[num] and i != start:
                i -= 1
            a_list.insert(i, a_list.pop(num))
        else:
            break
    return a_list


def merge(a_list, start1, stop1, start2, stop2):
    left_list = a_list[start1:stop1+start1]
    right_list = a_list[start2:stop2+start2]
    main_id = start1
    left_id = 0
    right_id = 0
    while left_id < len(left_list) and right_id < len(right_list) and main_id < len(a_list):
        if left_list[left_id] <= right_list[right_id]:
            a_list[main_id] = left_list[left_id]
            left_id += 1
        else:
            a_list[main_id] = right_list[right_id]
            right_id += 1
        main_id += 1
    while left_id < len(left_list) and main_id < len(a_list):
        a_list[main_id] = left_list[left_id]
        left_id += 1
        main_id += 1
    while right_id < len(right_list) and main_id < len(a_list):
        a_list[main_id] = right_list[right_id]
        right_id += 1
        main_id += 1
    return a_list


def timsort(a_list):
    minrun = get_minrun(len(a_list))
    runs = []
    for i in range(0, len(a_list), minrun):
        a_list = insertion_sort(a_list, i, minrun+i)
        runs.append([i, len(a_list[i:minrun+i])])
    runs_id = len(runs) - 1
    i = 1
    while len(runs) > 1:
        if len(runs) > 2:
            if runs[i-1][1] <= runs[i+1][1]:
                a_list = merge(a_list, runs[i-1][0], runs[i-1][1], runs[i][0], runs[i][1])
                runs[i-1] = [runs[i-1][0], runs[i-1][1] + runs[i][1]]
                runs.pop(i)
            elif runs[i-1][1] > runs[i+1][1]:
                a_list = merge(a_list, runs[i][0], runs[i][1], runs[i+1][0], runs[i+1][1])
                runs[i] = [runs[i][0], runs[i+1][1] + runs[i][1]]
                runs.pop(i+1)
        else:
            a_list = merge(a_list, runs[i-1][0], runs[i-1][1], runs[i][0], runs[i][1])
            runs[i-1] = [runs[i-1][0], runs[i-1][0] + runs[i][1]]
            runs.pop(i)
        i = 1 if i >= len(runs) - 2 else i + 1
    return a_list

        
