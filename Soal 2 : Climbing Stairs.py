from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        ways = [0] * (n + 1)
        
        ways[1] = 1
        ways[2] = 2
        
        for i in range(3, n + 1):
            ways[i] = ways[i-1] + ways[i-2]
            
        return ways[n]

if __name__ == "__main__":
    solusi = Solution()
    
    hasil = solusi.climbStairs(int(input()))
    print(hasil)
