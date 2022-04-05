# -*- coding: utf-8 -*-
from abc import *
from typing import TypeVar
from Dlink import *
E = TypeVar('E')

class Aqueue(metaclass=ABCMeta):
    
    @abstractmethod
    def push(self,item:E):
        pass

    @abstractmethod
    def pop(self)->E:
        pass

    @abstractmethod
    def front(self)->E:
        pass

    @abstractmethod
    def rear(self)->E:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def empty(self)-> bool:
        pass