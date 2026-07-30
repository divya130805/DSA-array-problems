def func(arr):
    mini=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<mini:
            mini=arr[i]
    return mini
print(func([1,2,3,4,5,6,7,8]))