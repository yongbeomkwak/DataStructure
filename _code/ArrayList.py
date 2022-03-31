# -*- coding: utf-8 -*-

from turtle import pos
from List import *
from ListIterator import *
import numpy as np


class ArrayList(List):
    DefaultSize:int=10
    data=None

    def __init__(self,size=DefaultSize):
        ArrayList.data=np.zeros(size*2) #더블링 기법
        self.listSize=0
    #클래스 메서드(class method)란 객체가 아닌 클래스 자체에 묶여있는(bound to) 메서드이다. 
    # 또다른 생성자 선언
    @classmethod
    def from_size(cls,size):
 
        ArrayList.data=np.zeros(size)       
        return cls(size)  #cls로  __init__으로 넘겨준 후 리턴
    
    def length(self):
        return self.listSize

    def clear(self):
        self.listSize=0
    
    def update(self,pos:int,item:E):
        ArrayList.data[pos]=item
    
    def getValue(self,pos:int):
        return ArrayList[pos]
    
    def append(self,item:E):
        ArrayList.data[self.listSize]=item
        self.listSize+=1
    
    def insert(self,pos:int,item:E):
        # 끝에부터 포스 앞까지 뒤로 당김
        for i in range (self.listSize,pos,-1):
            
            ArrayList.data[i]=ArrayList.data[i-1]

        ArrayList.data[pos]=item
        self.listSize+=1

    def remove(self,pos:int):
        ret=ArrayList.data[pos]

        
        # 왼쪽으로 옮기기 
        for i in range(pos,self.listSize):
            ArrayList.data[i]=ArrayList.data[i+1]

        self.listSize-=1 #사이즈 감소


        return ret

    def listIterator(self) -> ListIterator: #반복자 
        return self.ArrayListIterator(self) #바깥 클래스 전달
    

    class ArrayListIterator(ListIterator):

        def __init__(self,outer):
            self.outer:ArrayList=outer
            self.pos:int=0
        
        def hasNext(self) -> bool:
            return self. pos < self.outer.listSize
        
        def next(self) -> E:
            tmp= self.outer.data[self.pos] 
            self.pos+=1
            return tmp
        
        def hasPrevious(self) -> bool:
            return self.pos>0
        
        def previous(self) -> E:
            self.pos-=1
            return self.outer.data[pos]



