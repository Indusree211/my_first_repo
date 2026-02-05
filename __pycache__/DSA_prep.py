def find_max_min(arr): 
   return max(arr), min(arr) 
 
arr = [3, 1, 5, 2, 4] 
print(find_max_min(arr)) 

def min_max_arr(arr):
    max=min=arr[0]
    for num in arr:
        if num > max:
            max= num
        if num < min:
            min = num
    return max, min

arr = [3, 1, 5, 2, 4]
print(min_max_arr(arr))

def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

arr = [3, 1, 5, 2, 4]
print(second_largest(arr))

def second_smallest(arr):
    first = second = float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second

arr = [3, 1, 5, 2, 4]
print(second_smallest(arr))

def second_largest_smallest(arr): 
   arr = sorted(set(arr)) 
   return arr[-2], arr[1] 
 
arr = [4, 2, 1, 3, 5] 
print(second_largest_smallest(arr)) 


def reverse_array(arr): 
   return arr[::-1] 
 
arr = [1, 2, 3, 4, 5] 
print(reverse_array(arr)) 

def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array_in_place(arr))



def move_zeros_optimal(arr): 
   if not arr: 
       return arr 
 
   pos = 0 
   for i in range(len(arr)): 
       if arr[i] != 0: 
           arr[pos], arr[i] = arr[i], arr[pos] 
           pos += 1 
 
   return arr 


def missing_sum(arr):
    n = len(arr) + 1
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual

# VS Code call
print(missing_sum([1, 2, 4, 5]))

# Find Duplicate Elements and display only unique
def find_duplicates(arr):
    seen, dup = set(), set()
    for x in arr:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return list(dup)

#Function Call
arr = [1, 2, 3, 2, 4, 1, 5]
 
result = find_duplicates(arr)
 
print("Duplicate elements:", result)


def merge_sorted(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    return res + a[i:] + b[j:]
# ---- Function Call ----
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
 
merged = merge_sorted(a, b)
print("Merged Array:", merged)



def two_sum(nums, target): 
   mp = {} 

   for i, num in enumerate(nums):
    #    print("Current number:", num, "at index", i)
       if target - num in mp:
        #    print("Found:", target - num, "at index", mp[target - num])
           return [mp[target - num], i] 
       mp[num] = i
    #    print(mp)

# VS Code call
print(two_sum([2,7,11,15], 9)) 
 

