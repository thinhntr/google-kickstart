#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vt;
typedef vector<vector<int>> vvt;
typedef vector<string> vs;

#define repeat(ix, T) for (int ix = 0; ix < T; ++ix)
#define FOR(ix, s, e) for (int ix = s; ix < e; ++ix)
#define FORR(ix, s, e) for (int ix = s; ix > e; --ix)
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
#define prs(result) cout << "Case #" << order << ": " << result << endl;
template <class T>
void printarr(const vector<T> &ar)
{
    for (auto iter = ar.begin(); iter < ar.end() - 1; ++iter)
    {
        cout << *iter << " ";
    }
    cout << *(ar.end() - 1);
}

int MOD = int(1e9 + 7);

int num(char c)
{
    return c - 96;
}

void solve(int order)
{
    readint(N);
    readint(K);
    readstr(S);
    if (N == 1)
    {
        prs(num(S[0]) - 1);
        return;
    }
    if (N == 2)
    {
        if (S[0] < S[1])
        {
            prs(num(S[0]));
        }
        else
        {
            prs(num(S[0]) - 1);
        }
        return;
    }

    int mid = N / 2 - !(N & 1);
    long long total = 0;
    if (N & 1)
    {
        bool allGood = true;
        FORR(i, mid - 1, -1)
        {
            int opi = N - 1 - i;
            if (S[i] >= S[opi])
            {
                allGood = false;
                break;
            }
        }
        total = num(S[mid]) - (allGood ? 0 : 1);
    }
    else
    {

        int opi = N - 1 - mid;
        int curr = num(S[mid]) - ((S[mid] < S[opi]) ? 0 : 1);
        total = curr;
    }

    FORR(i, mid - 1, -1)
    {
        int opi = N - 1 - i;
        int curr = num(S[i]) - 1;
        long long coef = 1;
        if (curr > 0)
        {
            FOR(j, 0, mid - i)
            {
                coef = (K * coef) % MOD;
            }
        }
        total = (coef * curr % MOD + total) % MOD;
    }

    prs(total);
}

int main()
{
    readint(T);
    repeat(t, T) solve(t + 1);
    return 0;
}
