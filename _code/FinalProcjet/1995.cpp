#include <bits/stdc++.h>

using namespace std;

typedef struct _NODE
{
    char left, right;
} node;

unordered_map<char, node> tree; // tree, key:root , value: node(left,right);

void visit(char c)
{
    cout << c;
}

void preorder(char c)
{
    if (c == '.')
        return;
    visit(c);
    preorder(tree[c].left);
    preorder(tree[c].right);
}

void inorder(char c)
{
    if (c == '.')
        return;
    inorder(tree[c].left);
    visit(c);
    inorder(tree[c].right);
}

void postorder(char c)
{
    if (c == '.')
        return;
    postorder(tree[c].left);
    postorder(tree[c].right);
    visit(c);
}

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    char root;

    for (int i = 0; i < n; i++)
    {
        char rn, ln, r; //오른쪽,왼쪽,루트
        cin >> r >> ln >> rn;
        if (i == 0)
            root = r;       //첫 반복일 때 root노드 값 기억
        tree[r] = {ln, rn}; //해당 루트와 자식노드들을 기억
    }

    preorder(root);
    cout << endl;
    inorder(root);
    cout << endl;
    postorder(root);
}
