def func(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
print(func([1,2,3,4,5,6,7,8]))