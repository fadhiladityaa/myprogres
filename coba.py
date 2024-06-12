def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    
print(linear_search([1,23,42,342,11,1,34,1,41,6,1,41,3141,3], 3))

# arr = [12,13,1,3,14,24,2,414,2,52]
# print(arr[4])