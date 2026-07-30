def func(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
print(func([1,2,3,3,4,5,6,6]))