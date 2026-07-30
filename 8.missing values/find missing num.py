def func(arr):
    n=len(arr)+1
    exp=(n*(n+1))//2
    act=sum(arr)
    missing=exp-act
    return missing
print(func([1,2,4,6]))