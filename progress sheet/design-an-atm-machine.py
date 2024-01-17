class ATM:

    def __init__(self):
        self.dict = Counter()
        self.order = [20,50,100,200,500]
        
    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(len(banknotesCount)):
            if banknotesCount[i]==0:
                continue
            self.dict[self.order[i]]+=banknotesCount[i]  

    def withdraw(self, amount: int) -> list[int]:
        prev = self.dict.copy()
        keys = set(list(self.dict.keys()))
        notes =[]
        rem = amount
        if rem>=500 and 500 in keys:
            times = int(min(rem//500,self.dict[500]))
            if times>0:
                notes.append(times)
                rem-=(times*500)
                self.dict[500]-=times
            if self.dict[500]==0:
                del self.dict[500]
        else:
            notes.append(0)
        keys = set(list(self.dict.keys()))
        if rem>=200 and 200 in keys:
            times = int(min(rem//200,self.dict[200]))
            if times>0:
                notes.append(times)
                rem-=(times*200)
                self.dict[200]-=times
            if self.dict[200]==0:
                del self.dict[200]
        else:
            notes.append(0)
        keys = set(list(self.dict.keys()))
        if rem>=100 and 100 in keys:
            times = int(min(rem//100,self.dict[100]))
            if times>0:
                notes.append(times)
                rem-=(times*100)
                self.dict[100]-=times
            if self.dict[100]==0:
                del self.dict[100]
        else:
            notes.append(0)
        keys = set(list(self.dict.keys()))
        if rem>=50 and 50 in keys:
            times = int(min(rem//50,self.dict[50]))
            if times>0:
                notes.append(times)
                rem-=(times*50)
                self.dict[50]-=times
            if self.dict[50]==0:
                del self.dict[50]
        else:
            notes.append(0)
        keys = set(list(self.dict.keys()))
        if rem>=20 and 20 in keys:
            times = int(min(rem//20,self.dict[20]))
            if times>0:
                notes.append(times)
                rem-=(times*20)
                self.dict[20]-=times
            if self.dict[20]==0:
                del self.dict[20]
        else:
            notes.append(0)
        if rem!=0:
            self.dict = prev
            return [-1]
        else:
            return notes[::-1]
