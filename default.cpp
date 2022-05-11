/*
  Freedom of action
  @file: 0x3f.cpp
  @School: HTU
  @version: c++17
  @author: A_king
*/
#pragma GCC optimize(3)
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/trie_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace __gnu_pbds;
using namespace std;
void INIT();
namespace Template {
    #define IOS ios::sync_with_stdio(false);cin.tie(nullptr)
    #define FREOPEN freopen("in.in", "r", stdin);freopen("out.out", "w", stdout)
    #define out(x...) cout << #x <<" => ";Println(x);
    #define endl '\n'
    #define pb push_back
    #define pf push_front
    #define len(container) (int)(container).size()
    #define all(container) (container).begin(), (container).end()
    #define rall(container) (container).rbegin(), (container).rend()
    #define YES puts("YES")
    #define Yes puts("Yes")
    #define yes puts("yes")
    #define NO puts("NO")
    #define No puts("No")
    #define no puts("no")
    #define lb(container, val) (lower_bound(all(container), val) - container.begin())
    #define ub(container, val) (upper_bound(all(container), val) - container.begin())
    const int mod = 998244353;const double PI = acos(-1.0);const double eps = 1e-6;const int inf = 0x3f3f3f3f;const long long INF = 0x3f3f3f3f3f3f3f3f;
    template<typename T>T ksm(T a, long long b) {T res = 1;while (b) {if (b & 1) res *= a;a *= a;b >>= 1;}return res;}
    template<int MOD = mod> struct modint {
        int x;
        int Mod(int x) {if (x < 0) x += MOD;if (x >= MOD) x -= MOD;return x;}
        modint(int x = 0) : x(Mod(x)) {}
        modint(long long x) : x(Mod(x % MOD)) {}
        int val() const {return x;}
        modint operator-() const {modint T(MOD - x);return T;}
        modint inv() const {assert(x != 0);return ksm(*this, MOD - 2);}
        modint inverse() const {int a = x, b = MOD, u = 1, v = 0;while (b) {int t = a / b;a -= t * b;a ^= b ^= a ^= b;u -= t * v;u ^= v ^= u ^= v;}if (u < 0) u += MOD;return u;}
        modint &operator*=(const modint &T) {x = (long long)(x) * T.x % MOD;return *this;}
        modint &operator+=(const modint &T) {x = Mod(x + T.x);return *this;}
        modint &operator-=(const modint &T) {x = Mod(x - T.x);return *this;}
        modint &operator/=(const modint &T) {return *this *= T.inverse();}
        modint &operator++(int) {return *this = *this + 1;}
        modint &operator--(int) {return *this = *this - 1;}
        bool operator==(const modint &T) const {return x == T.x;}
        bool operator!=(const modint &T) const {return x != T.x;}
        bool operator<(const modint &T) const {return x < T.x;}
        bool operator>(const modint &T) const {return x > T.x;}
        friend modint operator*(const modint &T, const modint &Y) {modint res = T;res *= Y;return res;}
        friend modint operator+(const modint &T, const modint &Y) {modint res = T;res += Y;return res;}
        friend modint operator-(const modint &T, const modint &Y) {modint res = T;res -= Y;return res;}
        friend modint operator/(const modint &T, const modint &Y) {modint res = T;res /= Y;return res;}
        friend ostream &operator<<(ostream &o,const modint& T) {return o << T.x;}
    };
    typedef trie<string, null_type, trie_string_access_traits<>, pat_trie_tag, trie_prefix_search_node_update> TRIE;
    template<typename T> using RB = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
    template<typename T> using Q = __gnu_pbds::priority_queue<T, greater<T>, pairing_heap_tag>;// point_iterator
    typedef long long ll;typedef unsigned long long ull;typedef pair<double, double> PDD;typedef pair<ll, ll> PLL;typedef pair<int, int> PII;typedef pair<int, PII> PIII;
    template<typename T> using vc = vector<T>;template<typename T> using vvc = vc<vc<T>>;
    template<typename T> inline T Max(T &a, T b){if (a < b) a = b;return a;}template<typename T> inline T Max(T &a, T b, T c){a = Max(a, b);a = Max(a, c);return a;}
    template<typename T> inline T Min(T &a, T b){if (a > b) a = b;return a;}template<typename T> inline T Min(T &a, T b, T c){a = Min(a, b);a = Min(a, c);return a;}
    template<typename T> inline T Abs(T a){if (a < 0) a = -1 * a;return a;}
    template<typename T>T Gcd(T a, T b){return b ? Gcd(b, a % b) : a;}
    template<typename T> inline void Swap(T &a, T &b){a ^= b ^= a ^= b;}
    template<typename T> inline T Sum(vector<T> x) {return accumulate(all(x), 0ll);}
    template<typename T> inline T maxe(vector<T> x) {return *max_element(all(x));}template<typename T> inline T maxi(vector<T> x) {return max_element(all(x)) - x.begin();}
    template<typename T> inline T mine(vector<T> x) {return *min_element(all(x));}template<typename T> inline T mini(vector<T> x) {return min_element(all(x)) - x.begin();}
    template<typename T> inline int popcount(T x) {return __builtin_popcount(x);}template<typename T> inline int clz(T x) {return __builtin_clz(x);}
    template<typename T> inline void read(T &x) {x = 0;short sgn = 1;char c = getchar();while (c < 48 || 57 < c) {if (c == 45) sgn = -1;c = getchar();}while (48 <= c && c <= 57) {x = (x << 3) + (x << 1) + c - 48;c = getchar();}x *= sgn;}
    template<typename T, typename... Args> void read(T &first, Args& ... args) {read(first);read(args...);}
    inline ll read() {ll x = 0;short sgn = 1;char c = getchar();while (c < 48 || 57 < c) {if (c == 45) sgn = -1;c = getchar();}while (48 <= c && c <= 57) {x = (x << 3) + (x << 1) + c - 48;c = getchar();}x *= sgn;return x;}
    template<typename ...U>void Println(U... u) {int last_index = sizeof...(U) - 1, index = 0;auto printer = [last_index, &index]<typename Args>(Args args){if (last_index == index++) cout << args << endl;else cout << args << ", ";};(printer(u), ...);}
}using namespace Template;using Z = modint<>;// 998244353 1000000007
const int N = 1e6 + 10, M = 2e6 + 10;



void solve(int group_Id) {
    
}

signed main()
{
#ifdef A_king
    FREOPEN;
    clock_t CLOCK = clock();
#endif
    int T_case;read(T_case);
    // int T_case = 1;
    INIT();for (int i = 1;i <= T_case;i ++) solve(i);
#ifdef A_king
    cerr << "Run Time: " << (double)(clock() - CLOCK) / CLOCKS_PER_SEC * 1000 << " ms" << endl;
#endif
    return 0;
}
void INIT() {
    
    return ;
}

