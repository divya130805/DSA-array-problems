def func(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=((low+high)//2)
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
print(func([1,2,3,4,5,6,7,8],5))

