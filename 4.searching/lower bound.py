def func(arr,key):
    low=0
    high=len(arr)-1
   
    while low<=high:
        mid=((low+high)//2)
        if arr[mid]>key:
            high=mid-1
        
        else:
            low=mid+1

    return low
print(func([1,2,3,3,3,3,3,3,4,5,6,7,8],3))