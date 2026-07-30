def func(arr):
    pos=[]
    neg=[]
    for i in arr:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    result=[]
    i=j=0
    while i<len(pos) and j<len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i+=1
        j+=1
    while i<len(pos):
        result.append(pos[i])
        i+=1
    while j<len(neg):
        result.append(neg[j])
        j+=1
    return result

print(func([1,2,3,4,5,5,-1,-2,-3,-4,-5,-6,-9,-9]))
