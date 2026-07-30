def right_rotate(arr,k):
    n=len(arr)
    k=k%n
    temp=[0]*n
    for i in range(k):
        temp[i]=arr[n-k+i]
    for i in range(k,n):
        temp[i]=arr[i-k]
    for i in range(n):
        arr[i]=temp[i]
    return arr
print(right_rotate([1,2,3,4,5,6,7],4))