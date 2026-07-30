def func(arr):
    first=float('inf')
    second=float('inf')
    for i in arr:
        if i<first:
            second=first
            first=i
        elif i!=first and i<second:
            second=i
    if second==float('-inf'):
        return -1
    return second
print(func([1,2,3,4,5,6,7,8]))