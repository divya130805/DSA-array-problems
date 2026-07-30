def func(arr):
    leader=[]
    max_right=arr[-1]
    leader.append(max_right)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>=max_right:
            leader.append(arr[i])
            max_right=arr[i]
        return leader[::-1]
print(func([1,2,3,4,5,6,6,7,77,7]))