def func(arr):
    count=0
    maxi=0
    for i in arr:
        if i==1:
            count+=1
            maxi=max(maxi,count)
        else:
            count=0
    return maxi
print(func([1,2,1,1,1,1,1,1,1,1,1,1,11,1,1,1]))