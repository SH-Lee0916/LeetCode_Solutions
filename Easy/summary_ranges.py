'''
https://leetcode.com/problems/summary-ranges/
'''

class Solution:
    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))