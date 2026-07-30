def func(arr,index):
    result=[0]*len(arr)
    for i in range(len(arr)):
        result[index[i]]=arr[i]
    return result
print(func([1,2,3,4,5,6],[5,4,3,2,1,0]))