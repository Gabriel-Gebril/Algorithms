class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        i = 0
        j = 0
        seen = {}
        ans = 0
        l = len(s)

        while i < l and j < l:
            if(s[j] not in seen):
                seen[s[j]] = 1
                j = j + 1
                # j-i encodes the length of the current substring so I don't have to have a counter
                ans = max(ans, j - i)
            else:
                #move i pointer up 1 and delete the character the the pointer used to rest at.
                del seen[s[i]]
                i = i + 1

        return ans
