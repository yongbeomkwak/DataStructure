from BinaryTree import *
if __name__=="__main__":

    h3l1:Node = LNode("H3L1")
    h3r1:Node = LNode("H3R1")
    h3r2:Node = LNode("H3R2")
    h3r3:Node = LNode("H3R3")
    h2l1:Node = Node("H2L1",h3l1,h3r1)
    h2r1:Node = Node("H2R1",right=h3r2)
    h2r2:Node = Node("H2R2",right=h3r3)
    h1l1:Node = Node("H1L1",h2l1,h2r1)
    h1r1:Node = Node("H1R1",right=h2r2)
    h0:Node = Node("H0",h1l1,h1r1)
    
    btree=BinaryTree(h0)
    btree.preorder(btree.getRoot())
    # H0 H1L1 H2L1 H3L1 H3R1 H2R1 H3R2 H1R1 H2R2 H3R3 
    print()
    btree.inorder(btree.getRoot())
    #H3L1 H2L1 H3R1 H1L1 H2R1 H3R2 H0 H1R1 H2R2 H3R3
    print()
    btree.postorder(btree.getRoot())
    #H3L1 H3R1 H2L1 H3R2 H2R1 H1L1 H3R3 H2R2 H1R1 H0 


