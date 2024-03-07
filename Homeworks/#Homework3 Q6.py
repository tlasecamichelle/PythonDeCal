#Homework3 Q6

#for loop for minimum value
def find_min_for(arr):
    min_val = arr[0]
    for i in arr: 
        if i < min_val:
            min_val = i
    return min_val
print(find_min_for([2,0,11]))       #print statement #meow

#while loop for minimum value 
def find_min_while(arr) :
    if not arr:
        return None
    min_val = arr[0]
    i = 1 
    while i < len(arr) :
        if arr[i] < min_val : 
            min_val = arr[i]
        i += 1
    return min_val
print(find_min_while([2, 0, 11]))       #print statement

#for loop for maximum value
def find_max_for(arr) :
    if not arr :
        return None
    max_val = arr[0]
    for num in arr :
        if num > max_val :
            max_val = num
    return max_val
print(find_max_for([2, 0, 11]))     #print statement

#while loop for maximum value
def find_max_while(arr) :
    if not arr :
        return None
    max_val = arr[0]
    i = 1
    while i < len(arr) :
        if arr[i] > max_val :
            max_val = arr[i]
            i += 1
    return max_val
print(find_max_while([2, 0, 11]))
