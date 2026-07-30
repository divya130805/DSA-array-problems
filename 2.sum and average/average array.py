def func(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum//len(arr)


print(func([1,2,3,4,5,6,6,7,77,7]))