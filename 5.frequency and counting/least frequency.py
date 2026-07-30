def func(arr):
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    min_elem=min(freq,key=freq.get)
    print(min_elem)
print(func([1,1,1,2,3,3,3,3,4,5,6]))