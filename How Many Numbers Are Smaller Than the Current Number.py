 def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        buckets = [0]*102
        buckets = [0]*102
        #counting the numbers how many times are found
        for i in nums:
            buckets[i]  = buckets[i]+1
            # we have to sum it 
       # ading the bouckets
        for j in range(len(buckets)):
            buckets[j] += buckets[j-1]
        
        result = [None]*len(nums)   
        
        for i in range(len(nums)):
            if nums[i]== 0:
                result[i] = 0
            else:
                result[i] = buckets[nums[i]-1]
        return result   
                
