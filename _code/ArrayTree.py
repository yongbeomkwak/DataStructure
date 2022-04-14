import math
class ArrayTree:
    
    def __init__(self) -> None:
        self.tree=['A','B','C','D','E','F','G','H','I','J','K','L']
        self.size:int=len(self.tree)
    
    def parent(self,curr:int): # 해당 curr의 부모 찾기
        if(curr>0):
            return self.tree[math.floor((curr-1)/2)]
        else : 
            return "It is root"
    
    def leftchild(self,curr:int):
        #left=2n+1
        if(2*curr+1<self.size):
            return self.tree[2*curr+1]
        else:
            return "No left Child"
    
    def rightchild(self,curr:int):
        #right=2n+2
        if(2*curr+2<self.size):
            return self.tree[2*curr+2]
        else:
            return "No right Child"

    def leftSibling(self,curr):
        #left Sibling=n-1
        if(curr%2==0):
            return self.tree[curr-1]
        
        return "No left Sibling"
    
    def rightSibling(self,curr):
        #right sibling=n+1

        if(curr%2!=0 and curr+1<self.size):
            return self.tree[curr+1]

        return "No right Sibling" 

    

