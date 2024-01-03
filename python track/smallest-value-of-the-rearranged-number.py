class Solution:
    def smallestNumber(self, num: int) -> int:
        _strNum = str(num)
        if num == 0:
            return 0
        elif num>0:
            l = list(_strNum)
            li = [int(i) for i in l]
            li.sort()
            l,r = 0,1
            while li[0] == 0:
                if li[l] == 0 and li[r] != 0:
                    li[l],li[r] = li[r],li[l]
                    
                elif li[l] == 0 and li[r] == 0:
                    r+=1
                elif li[l] != 0 and li[r] == 0:
                    l+=1
                    r+=1
            ans = [str(i) for i in li]
            return int("".join(ans))

        elif num<0:
            _strNum = _strNum[1:]
            li = sorted([int(i) for i in _strNum],reverse=True)
           

            l = [str(i) for i in li ]
            l.insert(0,"-")
            
            return int("".join(l))

