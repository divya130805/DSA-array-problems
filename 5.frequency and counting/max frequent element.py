def func(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    max_ele=max(freq,key=freq.get)
    print(max_ele)
print(func([1,2,2,2,2,2,2,2,2,2,22,3,3,3,3,4,4,4,4,4,44,5,6]))