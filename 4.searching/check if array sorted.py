def func(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
print(func([1,2,3,4,5,6,7,8]))