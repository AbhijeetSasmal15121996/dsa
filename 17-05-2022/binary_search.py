# program assumes a sorted list
nums = [-1,0,3,5,9,12]
target = 5

def search(arr, s, i, j):
    tmp = int((i+j)/2)
    if j == 1:
        if arr[i] == s:
            return i
        else:
            return -1
    if i == j-1:
        return -1
    if arr[tmp] > s:
        return search(arr,s, i, tmp)
    elif arr[tmp] == s:
        return tmp
    else:
        return search(arr, s, tmp, j)


# Better soln
def search1( nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1



d = len(nums)
x = search(nums, target, 0, d)
print(x)