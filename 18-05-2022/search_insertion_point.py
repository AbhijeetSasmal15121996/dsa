def searchInsert(self, nums: List[int], target: int) -> int:
        left, right =0, len(nums) -1
        pivot = 0
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot -1
            elif nums[pivot] < target:
                left = pivot + 1
        if target > nums[pivot]:
            return left
        else:
            return right + 1