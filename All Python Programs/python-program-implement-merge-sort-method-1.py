def merge_sort(arr, start, end):
    if start >= end:
        return
 
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, end, mid)