class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 0

        for length in range(1, len(s) + 1):
            currentWord = s[:length]
            for word in wordDict:
                # print(length, currentWord)
                if length >= len(word) and currentWord.endswith(word) and dp[length - len(word)] == len(currentWord) - len(word):
                    dp[length] = length

        # print(dp)

        return True if dp[len(s)] != 0 else False
