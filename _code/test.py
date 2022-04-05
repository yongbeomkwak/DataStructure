from numpy import empty
from ArrayList import *
from LinkedList import *
from DoubleLinkedList import *
from Stack import *
from Link import *
from Queue import *
if __name__=="__main__":

    '''mylist2=ArrayList()
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
        print(iter.previous())'''
    
    '''
    mylist3=DoubleLinkedList()
    mylist3.append_front(6)
    mylist3.append_front(5)
    mylist3.append_front(4)
    mylist3.append_front(3)
    mylist3.remove(2) # 3 4 6
    mylist3.append_back(99) # 3 4 6 99
    mylist3.update(3,11) # 3 4 6 11  
    mylist3.pop_back() # 3 4 6 
    mylist3.pop_front() # 4 6
    
    iter3:ListIterator=mylist3.listIterator()

    while(iter3.hasPrevious()):
        print(iter3.previous(),end=' ')
'''

'''
st=Stack()

st.push(3)
st.push(2)
st.push(1)
st.pop()


while(not(st.empty())):
    print(st.pop())
'''

q=Queue()
q.push(1)
print(f'front: {q.front()}, rare: {q.rear()}')
q.push(2)
print(f'front: {q.front()}, rare: {q.rear()}')
q.push(3)
print(f'front: {q.front()}, rare: {q.rear()}')
q.clear()
print(f'front: {q.front()}, rare: {q.rear()}')

q.push(123)
q.push(456)
q.push("HAHA")

while(not(q.empty())):
    print(q.pop())

