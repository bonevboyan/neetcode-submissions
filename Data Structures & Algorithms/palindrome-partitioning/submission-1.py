class Solution:
    def isPalindrome(self, st):
        if len(st) == 1:
            return True
        
        left = 0
        right = len(st) - 1

        while right - left > 0:
            if st[left] != st[right]:
                return False
            left = left + 1
            right = right - 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def dfs(i, j):
            if i == len(s):
                if self.isPalindrome(current[j]):
                    result.append(current.copy())
                return
            
            latest = current[j]
            current[j] = current[j] + s[i]
            dfs(i + 1, j)

            if self.isPalindrome(latest):
                current[j] = latest
                current.append(s[i])
                dfs(i + 1, j + 1)
                current.pop()
            

        current.append(s[0])
        dfs(1, 0)
        return result


























        
    