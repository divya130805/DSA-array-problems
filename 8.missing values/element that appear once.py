def func(arr):
    ans=0
    for i in arr:
        ans^=i
    return ans
print(func([1,2,3,2,3]))