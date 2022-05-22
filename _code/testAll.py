from Sorting import *
if __name__=="__main__":
    
    a=[i for i in range(30,-1,-1)]
    s=Sorting(a)
    
    s.quickSort(a,0,len(a)-1)
    print(a)


    
