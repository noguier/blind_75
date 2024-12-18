class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         my_map = defaultdict(int)

         for num in nums:
            if num in my_map:
                return True
            else:
                my_map[num] +=1   
         return False