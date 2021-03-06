from abc import *
from typing import TypeVar

E = TypeVar('E')


class ListIterator(metaclass=ABCMeta):
    
    @abstractmethod
    def hasNext(self) ->bool:
        pass

    @abstractmethod
    def next(self) ->E:
        pass

    @abstractmethod
    def hasPrevious(self) ->bool:
        pass

    @abstractmethod
    def previous(self) ->E:
        pass

    