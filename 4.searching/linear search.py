def func(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    return False
print(func([1,2,3,4,5,6,7,8],0))