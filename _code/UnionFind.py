import sys

def union(p:list,a:int,b:int):
    pa:int=find(p,a)
    pb:int=find(p,b)
    if(pa<pb): # pa가 작으면 
        p[pb]=pa #pb의 부모를 pa로
    else:
        p[pa]=pb #pa의 부모를 pb


def find(p:list,a:int)->int:
    #root 찾기
    r=p[a]
    while(r!=p[r]): #부모를 계속 접근
        r=p[r]
    #root 찾음

    #path compression(시간 복잡도를 나중에 갈수록 줄이기 위해)
    c:int=a
    while(c!=p[c]): #root 도달 전까지
        pc=p[c] # 현재 c의 부모를 가르킴
        p[c]=r # c의 부모를 위에서 구한 최상위 root를 가르킴
        c=pc #c를 부모로 옮김

    return r


if __name__ =="__main__":
    n:int=0
    m:int=0
    n,m=map(int,input().split())

    p=[i for i in range(n+1)] #부모 배열 ,초기화는 자기자신
    

    for _ in range(m):
        oper,a,b=sys.stdin.readline().rstrip().split(" ")
        a=int(a)
        b=int(b)
        if(oper=="0"): #(Union)
            union(p,a,b)
        else: #Find
            pa:int=find(p,a)
            pb:int=find(p,b)
            if(pa==pb):
                print('YES')
            else:
                print('NO')