def movezero(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
print(movezero([1,0,2,0,3,0,4]))