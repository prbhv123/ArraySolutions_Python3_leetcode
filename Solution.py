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
    
        
