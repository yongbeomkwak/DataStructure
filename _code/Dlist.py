# -*- coding: utf-8 -*-
from abc import *
from typing import TypeVar

from ListIterator import *

E = TypeVar('E')

class Dlist:
    __metaclass__ = ABCMeta
    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def insert(self,pos:int,item:E):
        pass

    @abstractmethod
    def append_front(self,item:E):
        pass

    @abstractmethod
    def append_back(self,item:E):
        pass

    @abstractmethod
    def update(self,pos:int,item:E):
        pass
    
    @abstractmethod
    def getValue(self,pos:int)->E:
        pass
    
    @abstractmethod
    def pop_back(self)->E:
        pass

    @abstractmethod
    def pop_front(self)->E:
        pass

    @abstractmethod
    def remove(self,pos:int)->E:
        pass

    @abstractmethod
    def length(self) -> int: 
        pass
    
    @abstractmethod 
    def listIterator(self) -> ListIterator : #반복자 
        pass