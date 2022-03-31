# -*- coding: utf-8 -*-
from abc import *
from typing import TypeVar

from ListIterator import *

E = TypeVar('E')

class List(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def insert(self,pos:int,item:E):
        pass

    @abstractmethod
    def append(self,item:E):
        pass

    @abstractmethod
    def update(self,pos:int,item:E):
        pass
    
    @abstractmethod
    def getValue(self,pos:int):
        pass
    
    @abstractmethod
    def remove(self,pos:int):
        pass

    @abstractmethod
    def length(self) -> int: 
        pass
    
    @abstractmethod 
    def listIterator(self) -> ListIterator : #반복자 
        pass
    