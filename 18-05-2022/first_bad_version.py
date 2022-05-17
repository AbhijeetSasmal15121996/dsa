n = 2
i = 2
def isBadVersion(n):
    if n >= i:
        return True
    else:
        return False


def firstBadVersion1(n: int) -> int:
    left, right = 1, n
    if isBadVersion(1):
        return 1
    if isBadVersion(n) and not isBadVersion(n-1):
        return n
    while left <= right:
        pivot = left + (right - left) // 2        
        if isBadVersion(pivot) and not isBadVersion(pivot-1):
            return pivot
        elif isBadVersion(pivot) and isBadVersion(pivot-1):
            right = pivot
        else:
            left = pivot        

# Better Soln
def firstBadVersion(self, n: int) -> int:
    low = 1
    high = n
    while high > low:
        mid = (low + high) // 2
        if(isBadVersion(mid) == False):
            low = mid + 1
        else:
            high = mid
    return low



x = firstBadVersion(n)
print(x)