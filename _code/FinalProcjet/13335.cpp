#include <bits/stdc++.h>

using namespace std;

#define P pair<int, int>

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, L, W; // (n:트럭 수 L:다리 길이 W:견딜 수 있는 하중)
    cin >> n >> L >> W;

    queue<int> trucks; //트럭 담는 큐
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        trucks.push(tmp);
    }

    queue<P> q; // 무게,도착 시간
    int curr_weight = 0;
    int _time = 0;
    while (!q.empty() || !trucks.empty())
    {
        _time++; //시간 증가

        while (!q.empty() && _time == q.front().second) //현재시간이 도착시간과 같다면
        {
            curr_weight -= q.front().first; //현재 다리 무게 빼주고
            q.pop();                        //큐에서 제거
        }

        if (!trucks.empty() && curr_weight + trucks.front() <= W) //현재 가장 앞인 트럭무게 + 현재하중이 제한하중 이하면 다리를 건넌다
        {
            curr_weight += trucks.front();       //다리무게 증가
            q.push({trucks.front(), _time + L}); //다리 큐에 무게와 도착시간(현재시간+다리길이)을 넣어줌
            trucks.pop();                        //다리 올라갔으니 대기열 큐에서 제거
        }
    }

    cout << _time; //최종 시간 출력
}
