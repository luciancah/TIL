class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        temp = []
        result = ''

        for ch in s:
            if ch in vowels:
                temp.append(ch)
        
        for ch in s:
            if ch in vowels:
                result += temp.pop()
            else:
                result += ch
        
        return result
        