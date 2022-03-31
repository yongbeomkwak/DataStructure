from ArrayList import *
from LinkedList import *

if __name__=="__main__":

    mylist2=ArrayList()
    mylist2.append(3)
    mylist2.append(5)
    mylist2.append(6)
    mylist2.append(7)
    mylist2.append(8)
    mylist2.append(9)
    print(mylist2.data)
    iter2:ListIterator = mylist2.listIterator()
    while(iter2.hasNext()):
        print(int(iter2.next()))
    print("###################")
    myList=LinkedList()
    myList.append(3)
    print(myList.toString())
    myList.insert(0,1)
    print(myList.toString())
    myList.insert(0,4)
    print(myList.toString())
    myList.append(10)
    print(myList.toString())
    myList.insert(1,5)
    print(myList.toString())
    print("Remove value: ",myList.remove(1))
    print(myList.toString())
    print("Length: ",myList.length())
    iter:ListIterator=myList.listIterator()
    while(iter.hasNext()):
        print(iter.next())
    while(iter.hasPrevious()):
        print(iter.previous())
