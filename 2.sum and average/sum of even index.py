def func(arr):
    evensum=0
    for i in range(0,len(arr),2):
        evensum+=i
    return evensum

print(func([1,2,3,4,5,6,7,8]))