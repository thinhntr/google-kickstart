#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vt;
typedef vector<vector<int>> vvt;
typedef vector<string> vs;

#define repeat(T) for (int ct = 0; ct < T; ++ct)
#define fore(ar, e) for (int i = 0; i < e; ++i)
#define forse(ar, s, e) for (int i = s; i < e; ++i)

#define map(ar, dr, f)                  \
    for (int i = 0; i < dr.size(); ++i) \
        dr[i] = f(ar[i]);

#define readint(s) \
    int s;         \
    cin >> s;

#define readstr(s) \
    string s;      \
    getline(cin >> ws, s);

#define readints(ar, S)         \
    auto ar = vt();             \
    for (int i = 0; i < S; ++i) \
    {                           \
        int e;                  \
        cin >> e;               \
        ar.push_back(e);        \
    }

template <class T>
void printarr(const vector<T> &ar)
{
    for (auto iter = ar.begin(); iter < ar.end() - 1; ++iter)
    {
        cout << *iter << " ";
    }
    cout << *(ar.end() - 1);
}

void solve(int order)
{
    readint(N);
    readstr(S);
    auto score = vt(N);
    map(S, score, int);
    auto bin = vt(N);
    bin[0] = 1;
    forse(score, 1, N)
    {
        bin[i] = (score[i] > score[i - 1]) ? 1 + bin[i - 1] : 1;
    }

    cout << "Case #" << order + 1 << ": ";
    printarr(bin);
    cout << endl;
}

int main()
{
    readint(T);
    repeat(T) solve(ct);
    return 0;
}
