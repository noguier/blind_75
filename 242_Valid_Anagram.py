class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_map = defaultdict(int)
        for char in s:
            my_map[char] +=1
        # print(my_map)
        for char in t:
            if my_map[char] <= 0:
                return False
            my_map[char] -=1
        # print(my_map)
        return True
