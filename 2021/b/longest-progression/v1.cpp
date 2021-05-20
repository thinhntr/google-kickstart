#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vt;
typedef vector<vector<int>> vvt;
typedef vector<string> vs;

#define repeat(T) for (int ct = 0; ct < T; ++ct)

#define map(ar, dr, f)                \
  for (int i = 0; i < dr.size(); ++i) \
    dr[i] = f(ar[i]);

#define readint(s) \
  int s;           \
  cin >> s;

#define readstr(s) \
  string s;        \
  getline(cin >> ws, s);

#define readints(ar, S)       \
  auto ar = vt();             \
  for (int i = 0; i < S; ++i) \
  {                           \
    int e;                    \
    cin >> e;                 \
    ar.push_back(e);          \
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
  readints(A, N);
  cout << "Case #" << order + 1 << ": "
       << "result";
}

int ctoi(char c) { return int(c); }

int main()
{
  readint(T);
  repeat(T) solve(ct);
  return 0;
}
