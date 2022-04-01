# -*- coding: utf-8 -*-
from typing import TypeVar
E = TypeVar('E')

class Dlink():
    def __init__(self,item:E,prev,next):
        self.item:E=item
        self.prev:Dlink=prev
        self.next:Dlink=next