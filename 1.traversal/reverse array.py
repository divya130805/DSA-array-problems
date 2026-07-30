def func(arr):
    low=0
    high=len(arr)-1
    while (low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr

print(func([1,2,3,4,5,6,6,7,77,7]))