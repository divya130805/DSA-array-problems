def func(arr):
    maxi=arr[0]
    mini=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
   
   
        if arr[i]<mini:
            mini=arr[i]
    return  maxi,mini
print(func([1,2,3,4,5,6,7,8]))