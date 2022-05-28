#include <bits/stdc++.h>

using namespace std;

void print(list<char>&li)
{
    
    while(!li.empty())
    {
        cout << li.front();
        li.pop_front();
    }
    cout << endl;
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc;
    
    cin >> tc; 
    while(tc--)
    {
        list<char> li;
        string s;
        cin >> s;
        auto it=li.begin(); //커서의 위치
        for(const char&c:s)
        {
            if(c=='<') 
            {
                if(it!=li.begin()) //begin(가장 왼쪽이면) 더 이상 이동할 곳이 없으므로 예외처리
                {
                    it--; //왼쪽 이동 
                }
            }
            
            else if(c=='>')
            {
                if(it!=li.end()) it++; //마찬가지로 가장 오른쪽이면 이동 불가이므로 예외처리 
            }
            else if(c=='-')
            {
                if(li.empty()||it==li.begin()) continue; //비어있거나 왼쪽일 때 제거불가 

                
                auto tmp=li.erase(--it); //커서 왼쪽 위치 제거 
                //여기서 중요한점은 erase함수는 해당 위치 제거후 바로 다음 위치를 리턴 해줌 
                it=tmp; //해당 위치를 커서가 가르키게함
             
            }
            else
            {
                li.insert(it,c); //해당 커서위치에 문자 삽입 
            }
        }
        print(li); //최종 출력 
        
    }
}
