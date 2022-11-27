class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        idx = nums.index(k)
        nums = [1 if x > k else -1 for x in nums]
        nums[idx] = 0
        left = nums[:idx]
        right = nums[idx+1:][::-1]
        
        lsum = [0]
        rsum = [0]
        
        for x in left:
            lsum.append(lsum[-1] + x)
        for x in right:
            rsum.append(rsum[-1] + x)

        print(lsum)
        print(rsum)
        
        lsum = Counter(lsum)
        rsum = Counter(rsum)
        
        res = 0
        for k,v in lsum.items():
            res += rsum[-k] * v
        for k,v in lsum.items():
            res += rsum[1-k] * v

        print()
        return res        
            
        
        
#         print(left)
#         print(right)
        
        
        