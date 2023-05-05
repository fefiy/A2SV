  if target not in  nums:
            return []
        nums.sort()
        index = nums.index(target)
        indexs = []
        for i in range(index, len(nums), 1):
            if nums[i]== nums[index]:
                indexs.append(i)
            else:
                break    
        return  indexs
