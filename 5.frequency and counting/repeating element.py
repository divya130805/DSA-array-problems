def func(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for key,value in freq.items():
        if value>1:
            print(key)
print(func([1,2,3,3,4,4,5,5,6,7,7]))