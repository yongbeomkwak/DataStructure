#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    priority_queue<int> pq; //선물 보따리
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        if (tmp == 0) //입력이 0이고
        {
            if (pq.empty())
                cout << -1 << endl; //선물 보따리가 비어있다면 -1
            else
            {
                cout << pq.top() << endl; //그렇지 않으면 가장 가치가 높은(가장 위에있는 것)
                pq.pop();                 // 제거
            }
        }
        for (int j = 0; j < tmp; j++) //아닐 경우 선물 담기
        {
            int gift;
            cin >> gift;
            pq.push(gift);
        }
    }
}
