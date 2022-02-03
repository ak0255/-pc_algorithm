#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
// #include <bits/stdc++.h>
using namespace std;
#define inf 0x3f3f3f3f
#define IOS ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define FREOPEN freopen("in.in", "r", stdin);freopen("out.out", "w", stdout)
#define endl '\n'
namespace Template {
    typedef long long ll;
    typedef pair<int, int> PII;
    typedef pair<int, PII> PIII;
    typedef vector<int> VI;
    typedef vector<VI> VVI;
    typedef vector<ll> VL;
    typedef vector<VL> VVL;
    typedef vector<PII> VP;
    template<typename T> inline T Max(T &a, T b){if (a < b) a = b;return a;}
    template<typename T> inline T Max(T &a, T b, T c){a = Max(a, b);a = Max(a, c);return a;}
    template<typename T> inline T Min(T &a, T b){if (a > b) a = b;return a;}
    template<typename T> inline T Min(T &a, T b, T c){a = Min(a, b);a = Min(a, c);return a;}
    template<typename T> inline T Abs(T a){if (a < 0) a = -1 * a;return a;}
    template<typename T>T Gcd(T a, T b){return b ? Gcd(b, a % b) : a;}
    template<typename T> inline void Swap(T &a, T &b){T temp = a;a = b;b = temp;}
    template<typename T> inline void read(T &x) {
        x = 0;short sgn = 1;char c = getchar();
        while (c < 48 || 57 < c) {if (c == 45) sgn = -1;c = getchar();}
        while (48 <= c && c <= 57) {x = (x << 3) + (x << 1) + c - 48;c = getchar();}
        x *= sgn;
    }
    template<typename T, typename... Args> void read(T &first, Args& ... args) {
        read(first);read(args...);
    }
    template<typename ...U>void Println(U... u) {
        int last_index = sizeof...(U) - 1, index = 0;
        auto printer = [last_index, &index]<typename Args>(Args args){
            if (last_index == index++) cout << args << endl;
            else cout << args << ", ";};
        (printer(u), ...);
    }
}
using namespace Template;

const int N = 1e6 + 10, M = 2e6 + 10, mod = 1e9 + 7;



void solve(int group_Id) {
    
}

signed main()
{
    // IOS;
    FREOPEN;
    // int T;read(T);
    int T = 1;
    for (int i = 1;i <= T;i ++) solve(i);
    return 0;
}
