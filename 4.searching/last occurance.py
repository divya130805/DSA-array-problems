def func(arr,key):
    low=0
    high=len(arr)-1
    ans=0
    while low<=high:
        mid=((low+high)//2)
        if arr[mid]==key:
            ans=mid
            low=mid+1
        elif(arr[mid]<key):
            low=mid+1
        else:
            high=mid-1

    return ans
print(func([1,2,3,3,3,3,3,3,4,5,6,7,8],3))