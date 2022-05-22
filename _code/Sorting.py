import copy
from turtle import right

from pandas import pivot
class Sorting:

    def __init__(self,arr:list):
        self.__list=arr
    

    def insertionSort(self)->list:
        tmp=copy.deepcopy(self.__list) # 깊은 복사

        for i in range(1,len(tmp)):
            for j in range(i,0,-1): #i를 기준으로 왼쪽으로 가며 i가 들어갈 자리를 찾는다. 
                if(tmp[j]>=tmp[j-1]): # 왼쪽에 있는 값이 작거나 같으면 넘어감 
                    continue
                self.swap(tmp,j,j-1) #왼쪽에 값이 클 때 스왑
    
        return tmp
    

    def bubbleSort(self)->list:
        #가장 큰 것을 오른쪽 끝으로 계속 밈
        tmp=copy.deepcopy(self.__list)
        
        for i in range(0,len(tmp)):
            for j in range(0,len(tmp)-1-i):#가장 큰겂을 (오른쪽)끝까지 미루기 때문에 미룬 횟수만큼 오른쪽 끝 위치를 왼쪽으로 당김
                if(tmp[j]<=tmp[j+1]):
                    continue
                self.swap(tmp,j,j+1)
        
        return tmp
    
    def selectionSort(self)->list:
        tmp=copy.deepcopy(self.__list)

        for i in range(0,len(tmp)-1): #현재 값
            currIdx:int=i
            for j in range(len(tmp)-1,i,-1): #끝 부분 부터 i앞 까지
                if(tmp[j]<tmp[currIdx]): #현재 가르키는 값이 더크면 바꿈 
                    currIdx=j
            
            self.swap(tmp,i,currIdx) #가장 작은놈을 가르키는 인덱스와 현재 인덱스랑 변경
        
        return tmp

    
    def shellSort(self):
        tmp=copy.deepcopy(self.__list)

        sub_list_gap=len(tmp)//2
        #서브 리스트 길이

        '''
        Pass1
        ▪ 위치가 n/2만큼 떨어진 값을 2개씩 묶어 n/2개의 서브리스트를 생성
        • 예) n = 16이면, 8개의 서브리스트 생성: (0,8), (1,9), ..., (7, 15) ▪ 각 서브리스트를 Insertion Sort로 정렬
        ● Pass2
        ▪ 위치가 n/4만큼 떨어진 값을 4개씩 묶어 n/4개의 서브리스트를 생성
        • 예) n = 16이면,4개의 서브리스트 생성: (0,4,8,12), (1,5,9,13), ... ▪ 각 서브리스트를 Insertion Sort로 정렬
        '''

        while(sub_list_gap>2):
            for j in range(0,sub_list_gap):
                self.insertionSort2(tmp,j,sub_list_gap)
            
            self.insertionSort2(tmp,0,1)
            sub_list_gap=sub_list_gap//2
    
        return tmp

    
    def insertionSort2(self,arr:list,start:int,incr:int):
        
        for i in range(start+incr,len(arr),incr):
            for j in range(i,0,-incr):
                if(arr[j]>=arr[j-incr]):
                    continue
                self.swap(arr,j,j-incr) 
    
    def merge(self,arr:list,start:int,mid:int,end:int):
        tmp=[ 0 for _ in  range(end-start+1)]
        left_idx:int =start #왼쪽 시작지점 
        right_idx:int =mid+1 #오른쪽 시작지점 
        k:int=0

        while(left_idx<=mid and right_idx<=end):
            if(arr[left_idx]<=arr[right_idx]): #왼쪽이 작을 시 
                tmp[k]=arr[left_idx] #왼쪽 삽입
                left_idx+=1
            else:
                tmp[k]=arr[right_idx] #오른쪽 삽입
                right_idx+=1
            k+=1

        # 만약 left_idx 가 mid를 넘었으면 오른쪽 배열이 남은 것
        entry:int = right if left_idx> mid else left_idx
        target:int = end if left_idx> mid else mid
        
        for i in range(entry,target+1): #나머지 것 옮기고 
            tmp[k]=arr[i]
            k+=1
        
        p:int=0
        for i in range(start,end+1): #최종 정렬된 것 본 배열에 옮기기
            arr[i]=tmp[p]
            p+=1
        


    def mergeSort(self,arr:list,start:int,end:int):
        if(start<end):
            mid=(start+end)//2
            self.mergeSort(arr,start,mid) #왼쪽
            self.mergeSort(arr,mid+1,end) #오른쪽
            self.merge(arr,start,mid,end) #병합
    
    def partition(self,arr:list,start:int,end:int):
        pivot:int=arr[end]
        i:int =start-1
        for j in range(start,end):
            if(arr[j]<=pivot): #pivot보다 작으면 왼쪽 영역을 넓힌 후 스왑
                i+=1
                self.swap(arr,i,j)
        
        pos:int =i+1 #마지막으로 왼쪽 영역을 넓히고 
        self.swap(arr,pos,end) #end를 해당 영역에 넣는다(실질적으로 바꾼다)
        return pos #이후 왼쪽영역 즉, 피벗 영역을 리턴한다

    


    def quickSort(self,arr:list,start:int,end:int):
        if(start<end):
            q:int=self.partition(arr,start,end) #피벗위치
            #print("pos: ",start,end,q)
            self.quickSort(arr,start,q-1) # start~ 피벗 전
            self.quickSort(arr,q+1,end) # 피벗 후 ~end까지






    def view(self):
        print(self.__list)
    
    def swap(self,arr:list,i:int,j:int):
        tmp=arr[i]
        arr[i]=arr[j]
        arr[j]=tmp
    