def func(arr):
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for key,value in freq.items():
        if value==1:
            print(key)
print(func([1,2,3,4,4,4,2,3,5,5,1,10]))