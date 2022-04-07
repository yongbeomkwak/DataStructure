from BinaryTree import *
from Node import *
if __name__=="__main__":
    
#     mylist3=DoubleLinkedList() #이중 연결 리스트 생성 
#     mylist3.append_front(6) # 앞에 6 
#     mylist3.append_front(5) # 앞에 5 (5,6)
#     mylist3.append_front(4) # 앞에 4 (4,5,6)
#     mylist3.append_front(3) # 앞에 3 (3,4,5,6)
#     mylist3.remove(2) #  2번째 삭제 (3 4 6) 
#     mylist3.append_back(99) # 뒤에 99추가  (3 4 6 99)
#     mylist3.update(3,11) # 3번째 11변환 (3 4 6 11)  
#     mylist3.pop_back() # 뒤에 제거  (3 4 6) 
#     mylist3.pop_front() # 앞에 제거 (4 6)
    
#     iter3:ListIterator=mylist3.listIterator()
#     iter1:ListIterator=mylist3.listIterator()
#     # 4<-6 
#     while(iter3.hasPrevious()):
#         print(f'{iter3.previous()}',end=' ') 
#     print()
#     # 4 -> 6
#     while(iter1.hasNext()): 
#         print(f'{iter1.next()}',end=' ') 
#     print()


# q=Queue()
# q.push(1)
# print(f'front: {q.front()}, rare: {q.rear()}')
# q.push(2)
# print(f'front: {q.front()}, rare: {q.rear()}')
# q.push(3)
# print(f'front: {q.front()}, rare: {q.rear()}')
# ## 3->2->1
# q.clear() #초기화
# print(f'front: {q.front()}, rare: {q.rear()}')

# q.push(123)
# q.push(456)
# q.push("HAHA")

# while(not(q.empty())):
#     print(f'Queue PoP: {q.pop()}')


# ast=ArrayStack()


# ast.push(3)
# ast.push(33)
# ast.push(333)

# '''
# 333
# 33
# 3
# '''
# while(not(ast.empty())):
#     print(f'stack pop: {ast.pop()}')

# print(f'Stack is emtpy? {ast.empty()}')
    root=Node(100)
    tree=BinaryTree(root)
    tree.insert_Node(root,Node(50))
    tree.insert_Node(root,Node(80))
    tree.insert_Node(root,Node(120))
    tree.insert_Node(root,Node(20))
    tree.insert_Node(root,Node(110))
    tree.insert_Node(root,Node(180))

    '''
                100
            50          120
        20      80   110    180
    '''

    print("Pre Order")
    tree.preorder(root)
    print("Post Order")
    tree.postorder(root)
    print("In Order")
    tree.inorder(root)


