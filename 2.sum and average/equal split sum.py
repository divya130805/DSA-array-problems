def fuc(arr):
    total=sum(arr)
    left=arr[0]
    for i in arr:
        left+=i
        right=total-left
    if left==right:
        return True
    return False
print(fuc([1,2,3,4,5,6,7,8]))