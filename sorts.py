# O(n ^ 2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(n ^ 2)
def insertion_sort(arr):
    l = arr[:]
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l

# O(n * log(n))
def quick_sort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    pivot = arr[0]
    l_arr, e_arr, h_arr = [], [], []
    for i in arr:
        if i < pivot:
            l_arr.append(i)
        elif i > pivot:
            h_arr.append(i)
        else:
            e_arr.append(i)
    return quick_sort(l_arr) + e_arr + quick_sort(h_arr)

# O(n * log(n))
# less memory, but ~3 times slower
# pure function
def quick_sort_pure(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    return quick_sort_pure(list(filter(lambda x: x < arr[0], arr))) + \
           list(filter(lambda x: arr[0] == x, arr)) + \
           quick_sort_pure(list(filter(lambda x: x > arr[0], arr)))

# O(n * log(n))
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    l, r = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
    len_l, len_r = len(l), len(r)
    i, j = 0, 0
    res = []
    while i != len_l or j != len_r:
        if i == len_l:
            res.append(r[j])
            j += 1
            continue
        if j == len_r:
            res.append(l[i])
            i += 1
            continue
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
            continue
        else:
            res.append(r[j])
            j += 1
            continue
    return res
