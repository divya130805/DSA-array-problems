def func(arr):
    n=len(arr)
    for i in range(0,n):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            print(arr[i])

print(func([1,2,3,4,5,6,7,8]))