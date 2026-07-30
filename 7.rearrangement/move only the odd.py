def func(arr):
    odd=[]
    for i in range(len(arr)):
        if arr[i]%2!=0:
            odd.append(arr[i])
    odd.reverse()
    j=0
    for i in range(len(arr)):
        if arr[i]%2!=0:
            arr[i]=odd[j]
            j+=1
    return arr
print(func([1,0,2,0,3,0,4]))