from typing import TypeVar
from abc import *

E = TypeVar('E')
K = TypeVar('K')

class Dictionary(metaclass=ABCMeta):

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def insert(self,key:K,e:E):
        pass

    @abstractmethod
    def remove(self,key:K)-> E:
        pass

    @abstractmethod
    def removeAny(self) -> E:
        pass

    @abstractmethod
    def find(self,key:K)->E:
        pass

    @abstractmethod
    def size(self)->int:
        pass