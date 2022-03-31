# -*- coding: utf-8 -*-

from typing import TypeVar

E = TypeVar('E')

class Link:

    def __init__(self,item:E,next):
        self.item:E=item
        self.next:Link=next