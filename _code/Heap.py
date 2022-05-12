from typing import TypeVar
E = TypeVar('E')

class MaxHeap:
    
    def __init__(self,arr:list,num:int,max:int) -> None:
        self.__Heap:list=arr
        self.__size:int=max
        self.__n:int=num
        self.buildHeap()
    
    def heapsize(self) -> int:
        return self.__size
    
    def isLeaf(self,pos:int)->bool:
        if(pos<self.__n and pos >= self.__n//2): #만약 pos가 n보다 작고, n/2 보다 크면 자식이 없는 Leaf이다
            return True
        return False
    
    def leftchild(self,pos:int) -> E:
        if(2*pos+1>=self.__n): #범위 넘었으면 
            return "Position has no left"
        return 2*pos+1
    
    def rightchild(self,pos:int) -> E:
        if(2*pos+2>=self.__n):
            return "Position has no right"
        return 2*pos+2
    
    def parent(self,pos:int)->E:
        if(pos<=0):
            return "Position has no parent"
        return (pos-1)//2 # 내림연산을 위해 -1 

    def swap(self,i:int,j:int):
        tmp:E=self.__Heap[i]
        self.__Heap[i]=self.__Heap[j]
        self.__Heap[j]=tmp

    def shiftDown(self,pos:int): #작은 노드는 아래로 
        
        if(pos<0 or self.__n<=pos): 
            return "Illegal heap position"

        while(not(self.isLeaf(pos))):
            j:int=self.leftchild(pos)
            if((j<(self.__n-1)) and ((self.__Heap[j])<self.__Heap[j+1])): #왼쪽이 오른쪽보다 작으면 
                j+=1 #오른쪽을 가르키게 한다.
            if(self.__Heap[pos]>=self.__Heap[j]):  #오른쪽보다 크거나 같으면 만족함, 탈출
                return
            #아니면 오른쪽과 바꿔줌(j)
            self.swap(pos,j)
            pos=j # pos역시 아래로 내려감
    
    def buildHeap(self):
        for i in range(self.__n//2-1,-1,-1): #자식을 갖고있는 부모 노드을 shiftDown 연산 진행
            self.shiftDown(i)
    
    def insert(self,val:E):
        
        if(self.__n>=self.__size):
            return "Heap is Full"
        curr:int=self.__n
        self.__Heap.append(val)
        self.__n+=1
        while((curr!=0) and  self.__Heap[curr]>self.__Heap[self.parent(curr)]): #민약 부모보다 크면 변경
            # Shift Up
            self.swap(curr,self.parent(curr))
            curr=self.parent(curr) 
    
    def removemax(self):
        if(self.__n<0): 
            return "No items"
        self.__n-=1
        self.swap(0,self.__n)
        if(self.__n!=0):
            self.shiftDown(0)
        return self.__Heap[self.__n]
    
    def isempty(self)->bool:
        if(self.__n<=0):
            return True
        return False
    
    def prt(self):
        print(self.__Heap)   
