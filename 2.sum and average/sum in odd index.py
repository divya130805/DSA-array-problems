def func(arr):
    odd=0
    for i in range(1,len(arr),2):
        odd+=i
    return odd
print(func([1,2,3,4,5,6,7,8]))
