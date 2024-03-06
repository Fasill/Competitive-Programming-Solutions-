class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        li = []
        for letter in letters:
            li.append(ord(letter))
        s = bisect_right(li,ord(target))
        if s<len(letters):
            
            return letters[s]
        return letters[0]