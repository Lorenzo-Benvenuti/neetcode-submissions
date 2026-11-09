class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        count = {}

        # Count frequencies of characters in the first string
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Match frequencies with the second string
        for char in t:
            # If the character is missing or its count drops below zero, it's not an anagram
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True
