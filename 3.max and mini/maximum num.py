def func(arr):
    maxi=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi
print(func([1,2,3,4,5,6,7,8]))