
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, ret, count = 0, 0, 0

        for i in range(len(nums)) : 
            if nums[i] == 0 :
                count += 1
            
            while count > 1 :
                if nums[left] == 0 :
                    count -= 1
                left += 1
            
            ret = max(ret, i - left + 1 - count)
    
        return ret - 1 if ret == len(nums) else ret
```

Basically this is the approach,

1. Have a right pointer ($i$ in this case) that increments
2. While this right pointer increments if a zero is encountered, increment the zero count
3. Then adjust the left pointer until the number of zero’s is maintained at 1
4. Then keep track of the max length
	1. The one edge case for a list of 1’s, would return a total length of `len - 1`.