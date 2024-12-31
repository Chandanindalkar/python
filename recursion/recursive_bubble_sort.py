nums = [8,5,7,2,10,3,4,1,6,9]

def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        return bubble_sort(arr[:-1]) + [arr[-1]]
    
print(bubble_sort(nums))