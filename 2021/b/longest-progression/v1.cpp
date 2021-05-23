#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vt;
typedef vector<vector<int>> vvt;
typedef vector<string> vs;

#define repeat(T) for (int ct = 0; ct < T; ++ct)
#define forrange(s, e) for (int i = s; i < e; ++i)
#define forrrange(s, e) for (int i = s; i > e; --i)
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

void solve(int order)
{
    readint(N);
    readints(A, N);
    if (N < 4)
    {
        prs(N);
        return;
    }
    auto D = vt(N);
    auto count = vt(N);

    D[0] = A[1] - A[0];
    count[0] = 1;
    int maxl = 0;

    forrange(1, N)
    {
        D[i] = A[i] - A[i - 1];
        count[i] = (D[i] != D[i - 1]) ? 1 : count[i - 1] + 1;
        maxl = max(maxl, count[i]);
    }

    forrrange(N - 1, -1)
    {
        if (count[i] == i + 1)
        {
            break;
        }
        int currentLength = count[i];
        while (count[i] > 1)
        {
            --i;
        }
        int type1 = currentLength + 2;
        int type2 = 0;
        int type3 = 0;
        int type4 = 0;
        if ((i - 3 >= 0) && (D[i - 3] == D[i]) && (A[i - 3] + D[i - 3] * 2 == A[i - 1]))
        {
            type2 = currentLength + count[i - 3] + 2;
            if (count[i - 3] < i - 3 + 1)
                ++type2;
        }
        if ((i == N - 1) || (i < N - 1) && (count[i + 1] == 1) && (D[i - 1] == D[i - 2]))
        {
            type3 = count[i - 1] + 1;
            if (count[i - 1] < i - 1 + 1)
                ++type3;
        }
        if (i - 2 >= 0 and A[i - 2] + D[i - 2] * 2 == A[i])
        {
            type4 = count[i - 2] + 2;
            if (count[i - 2] < i - 2 + 1)
                ++type4;
        }
        maxl = max(max(max(max(maxl, type1), type2), type3), type4);
    }

    prs(maxl);
}

int main()
{
    readint(T);
    repeat(T) solve(ct + 1);
    return 0;
}
