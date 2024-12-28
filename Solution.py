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

# Rotating the array by one
class Solution:
    def left_rotate_by_one(arr):
        n = len(arr)
        if n > 1:
            temp = arr[0]
            for i in range(1,n):
                arr[i-1] = arr[i]
                arr[n-1] = temp
        return arr
# Function to run test cases
def test_left_rotate():
    test_cases = [
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]),  # Basic test
        ([10, 20, 30], [20, 30, 10]),  # Small array
        ([1], [1]),  # Single element
        ([], []),  # Empty array
        ([5, 5, 5, 5], [5, 5, 5, 5])  # Identical elements
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        output = left_rotate_by_one(input_arr[:])  
        assert output == expected, f"Test case {i + 1} failed: {output} != {expected}"
        print(f"Test case {i + 1} passed!")

# Run the test cases
if __name__ == "__main__":
    test_left_rotate()
    print("All test cases passed!")

# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        # Reversing the entire array
        nums.reverse()
        # Reversing the array first k elements
        nums[:k] = reversed(nums[:k])
        # Reversing the array after k elements
        nums[k:] = reversed(nums[k:])

# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        n = len(nums)
        for i in range(n):
                if nums[i] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j +=1
                    
# Sorted Array Search
class Solution:
    def searchInSorted(self,arr, k):
        n = len(arr)
        for i in range (n):
            if (arr[i] == k):
                    return True
        return False
        
# Union of 2 Sorted with Duplicates 

## Brute force approach
class Solution:
    def findUnion(self,a,b):
        s = set()
        Union = []
        for num in a:
            s.add(num)
        for num in b:
            s.add(num)
        for num in s:
            Union.append(num)
        Union.sort()
        return Union
        
## Optimal approach
class Solution:
    def findUnion(self,a,b):
        i,j = 0, 0
        union = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])
                i+=1
            else:
                if len(union) == 0 or union[-1] != b[j]:
                    union.append(b[j])
                j+=1
        while i < len(a):
            if union[-1] != a[i]:
                union.append(a[i])
            i+=1
        while j < len(b):
            if union[-1] != b[j]:
                union.append(b[j])
            j+=1
                
        return union
        

    
        
