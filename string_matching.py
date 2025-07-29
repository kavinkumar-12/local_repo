class string_matching:
    def __init__(self,tl,pl):
        self.text=tl
        self.pattern=pl
        self.text_length=len(self.text)
        self.pattern_length=len(self.pattern)
    def find_index(self):
        text_end = self.text_length + 1 - self.pattern_length
        for k in range(0,text_end):
            count=0
            index_text=k
            for j in range(0,self.pattern_length):
                if self.pattern[j] == self.text[index_text] :
                    count+=1
                index_text+=1
            if count == self.pattern_length:
                print("the sub string found at index : ",end=" ")
                for i in range(0,self.pattern_length):
                    print(k+i,end=" ")

text=input("enter the text (space as underscore) : ")
pattern=input("enter the substring to the index of pattern in text : ")

sm = string_matching(text,pattern)
sm.find_index()