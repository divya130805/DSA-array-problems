def func(arr):
    even=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            even.append(arr[i])
    even.reverse()
    j=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]=even[j]
            j+=1
    return arr
print(func([1,2,3,4,5,6,7,8]))