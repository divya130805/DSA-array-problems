def count(arr):
    pos=neg=zero=0
    for i in arr:
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else:
            zero+=1
    return pos,neg,zero

print(count([1,2,3,4,5,6,7,8,9,0,1,2,3,8,4]))
