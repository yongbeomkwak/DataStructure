# -*- coding: utf-8 -*-
from abc import *
from typing import TypeVar
from Link import *
E = TypeVar('E')

class Astack(metaclass=ABCMeta):
    
    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def push(self,item:E):
        pass

    @abstractmethod
    def pop(self)->E:
        pass

    @abstractmethod
    def topValue(self)->E:
        pass

    @abstractmethod
    def length(self)->int:
        pass

    @abstractmethod
    def empty(self)->bool:
        pass