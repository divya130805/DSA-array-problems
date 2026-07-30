def func(arr):
    if not arr:
        return False
    maxi=max(arr)
    mini=min(arr)

    if maxi-mini+1 != len(arr):
            return False

    num=set(arr)
    for i in range(mini,maxi+1):
        if i not in arr:
            return False
    return True

print(func([1,2,3,4,5,6,6,7,77,7]))