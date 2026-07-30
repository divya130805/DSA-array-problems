def func(arr1,arr2):
    arr=sorted(arr1+arr2)
    n=len(arr)
    if n%2==1:
        print(arr[n//2])
    else:
        print(arr[n//2]+arr[n//2-1]/2)

print(func([1,2,3,4,5,6,7,8],[1,2,3,4,5,55,66,77]))