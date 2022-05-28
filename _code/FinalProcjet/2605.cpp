#include <bits/stdc++.h> //코테용 라이브러리 
using namespace std;

void print(list<int>&li) //최종 출력 함수
{
    
    while(!li.empty()) //앞에서 부터 꺼내 출력
    {
        cout << li.front() << " ";
        li.pop_front();
    }
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int stu_n;
    
    cin >> stu_n; //학생 수 
    list<int> li; //Linked List 생성 
    for(int i=1;i<=stu_n;i++)
    {
        int move;
        cin >> move; //이동 횟수 
        if(li.empty()) li.push_front(i); //첫 삽일 때는 무조건 앞에 
        else
        {
            auto it=li.begin(); //리스트의 앞을 가르키며 
            int shift=li.size()-move; //뒤에서 부터 몇번 앞으로가야하는지 
            while(shift-->0)it++; //반복자 이동 
            
            li.insert(it,i); //해당 반복자가 가르키는 위치에 해당 학생 번호 삽입
        }
    }
    
    print(li); //최종 출력

    return 0;
}
