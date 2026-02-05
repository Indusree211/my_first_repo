def min_max_arr(arr):
	min = max = arr[0]
	for num in arr:
		if num > max:
			max = num
		if num < min:
			min = num
	return min , max

print(min_max_arr([3, 1, 5, 2, 4]))


def second_max_min(arr):
	large = scnd_large = float('-inf')
	small = scnd_small = float('inf')
	for num in arr:
		if num > large:
			scnd_large = large
			large= num
		elif large > num> scnd_large:
			scnd_large = num
		
		if num < small:
		    scnd_small = small
		    small = num
		elif small < num < scnd_small:
			scnd_small = num
	return scnd_large, scnd_small

print(second_max_min([3, 1, 5, 2, 4]))


def rotate_arr_right(arr, k):
	n = len(arr)
	k %= n
	return arr[k:] + arr[:k]

print(rotate_arr_right([1, 2, 3, 4, 5], 2))


def rotate_arr_left(arr, k):
	n = len(arr)
	k %= n
	return arr[-k:] + arr[:-k]

print(rotate_arr_left([1, 2, 3, 4, 5], 2))

def rotate_left(self, nums: List[int], k: int) -> None:
        if not nums:
            return
        
        n = len(nums)
        k %= n
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

def reverse_arr(arr):
	left = 0
	right = len(arr)-1
	while left < right:
		arr[left], arr[right] = arr[right], arr[left]
		left +=1
		right -=1
	return arr
print(reverse_arr([1, 2, 3, 4, 5]))

def sort_012(arr):
    low = mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(sort_012([0, 1, 2, 0, 1, 2]))