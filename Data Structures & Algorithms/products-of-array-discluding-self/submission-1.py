class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # What if there were 2 zeros - All would be zero

        # What if there were only 1 zero - only the zero would have a value

        #What if there were no zeros - Everything shld be standard and we just add total and divede by num

        # How can we incompass all of this stuff

        # Step 1
        counter = {}
        tot = 1
        ztot = 1
        for num in nums:
            tot = tot * num
            if num != 0:
                ztot = ztot * num

            counter[num] = counter.get(num, 0) + 1

        result = []
        if 0 in counter:
            if counter[0] >= 2: # if their are multiple zeros

                result = [0] * len(nums)
                return result
            if counter[0] == 1:
                
                for num in nums: # If there is one zero
                    if num == 0:
                        result.append(ztot)
                    else:
                        result.append(0)
                return result
                
        for num in nums: # There are no zeros
            result.append(tot // num)

        return result



            

            
        