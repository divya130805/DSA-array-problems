def func(arr):
    even=odd=0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even ,odd

print(func([1,2,3,4,5,6,6,7,77,7]))