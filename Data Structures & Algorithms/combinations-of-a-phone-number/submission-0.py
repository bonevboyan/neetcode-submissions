class Solution:
    def digitToLetter(self, s):
        if s == '2':
            return ['a', 'b', 'c']
        if s == '3':
            return ['d', 'e', 'f']
        if s == '4':
            return ['g', 'h', 'i']
        if s == '5':
            return ['j', 'k', 'l']
        if s == '6':
            return ['m', 'n', 'o']
        if s == '7':
            return ['p', 'q', 'r', 's']
        if s == '8':
            return ['t', 'u', 'v']
        if s == '9':
            return ['w', 'x', 'y', 'z']
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        result = []
        current = []

        def dfs(i):
            nonlocal current
            if i == len(digits):
                result.append(''.join(current))
                return

            letters = self.digitToLetter(digits[i])
            for letter in letters:
                current.append(letter)
                dfs(i + 1)
                current.pop()

        dfs(0)

        return result
        
    

