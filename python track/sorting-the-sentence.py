class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        my_dict = {}
        for i in s:
            my_dict[int(i[-1])] = i[:-1]

        sorted_dict = sorted(my_dict.items())
        result = ''.join([value+' ' for key, value in sorted_dict])
        return result[:-1]