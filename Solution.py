# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n= len(nums)
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


# 1752. Check if Array Is Sorted and Rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n):
            if (nums[i] > nums[(i+1) % n]):
                count +=1
            if count > 1:
                return False
        return True
        
