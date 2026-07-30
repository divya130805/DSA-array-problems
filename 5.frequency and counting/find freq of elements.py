def func1(arr):
    visited=[]
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        print(arr[i], "->" ,count)
        visited.append(arr[i])
print(func1([1,2,3,3,3,3,4,5,6]))

# List
# ↓
# Take one element
# ↓
# Already visited?
# │
# ├── Yes → Skip
# │
# └── No
#       ↓
# Count how many times it appears
#       ↓
# Print frequency
#       ↓
# Add to visited
#       ↓
# Move to next element