#include <bits/stdc++.h>

#define MAX 51
using namespace std;

vector<int> tree[MAX];
int ans = 0;
int del;

bool search(const int node) //현재 노드 번호
{
    if (node == del) //만약 제거 될 노드면
    {
        return true; // true 리턴
    }
    if (tree[node].size() == 0)
        ans++;                                  //현재 자식이 0개면 리프노드
    for (int i = 0; i < tree[node].size(); i++) //자식 개수만큼 탐색 시작
    {
        bool isfind = search(tree[node][i]);

        if (isfind && tree[node].size() == 1)
            ans++;
        //탐색 결과가 해당 노드를 찾았고 자식이 해당 노드뿐이면 삭제 후
        //해당 노드는 리프 노드가 되므로 증가
    }

    return false;
}

int main()
{
    int n, root;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int parent;
        cin >> parent;
        if (parent == -1)
            root = i;
        else
        {
            tree[parent].push_back(i);
        }
    }
    cin >> del;
    search(root);

    cout << ans;
    return 0;
}
