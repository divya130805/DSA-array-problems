def func(arr,key):
    low=0
    high=len(arr)-1
    ans=0
    while low<=high:
        mid=((low+high)//2)
        if arr[mid]==key:
            return arr[mid]
        elif(arr[mid]<key):
            
            low=mid+1
        else:
            ans=arr[mid]
            high=mid-1

    return ans
print(func([1,2,3,3,3,3,3,3,4,5,6,7,8],7.5))