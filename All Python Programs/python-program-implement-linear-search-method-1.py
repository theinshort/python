def linear_search(alist, key):
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1