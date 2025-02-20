# Leetcode Question-1
# Two Sum (Easy)
# Link: https://leetcode.com/problems/two-sum/description/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    sol = []
    hash_map = {}
    for index, num in enumerate(nums):
        sec_num = target - num
        if sec_num not in hash_map.keys():
            hash_map[num] = index
        else:
            return [ hash_map.get(sec_num), index]
    print(hash_map)
    return sol

#print(twoSum([3,3], 6))
        

# Leetcode Question-2
# Reverse String (Easy)
# Link: https://leetcode.com/problems/reverse-string/description/
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # l,r = 0, len(s)-1
    # while l<=r:
    #     s[l], s[r] = s[r], s[l]
    #     l = l+1
    #     r = r-1

    n = len(s)
    for i in range(0, n//2):
        s[i], s[n-1-i] = s[n-i-1], s[i]
    print(s)

reverseString(["h","e","l","l","o"])