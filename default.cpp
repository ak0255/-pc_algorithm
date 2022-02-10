#include <bits/stdc++.h>
using namespace std;
namespace Template {
    #define inf 0x3f3f3f3f
    #define IOS ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
    #define FREOPEN freopen("in.in", "r", stdin);freopen("out.out", "w", stdout)
    #define endl '\n'
    #define pb push_back
    #define pf push_front
    #define len(x) (int)(x).size()
    #define all(x) (x).begin(), (x).end()
    const double PI = acos(-1);
    const double eps = 1e-6;
    typedef long long ll;
    typedef pair<double, double> PDD;
    typedef pair<int, int> PII;
    typedef pair<int, PII> PIII;
    typedef vector<int> VI;
    typedef vector<VI> VVI;
    typedef vector<ll> VL;
    typedef vector<VL> VVL;
    typedef vector<PII> VP;
    typedef vector<string> VS;
    typedef vector<VS> VVS;
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

// __builtin_popcount(x); 返回x中1的个数
// accumulate(begin(), end(), start_val); 数组求和
// min_element(begin(), end()); 最小元素的迭代器
// max_element(begin(), end()); 最大元素的迭代器
// minmax_element(begin(), end()); PII类型返回两个迭代器
// nth_element(begin(), begin() + k_th, end(), less<int>()); //下标从begin()开始，默认寻找第k小的数
// priority_queue<type, vector<type>, greater<type>> q; 大根堆，重载大于号
// map<key, value> key -> PII √, unordered_map可能导致二次时间复杂度
clock_t CLOCK = clock();
const int N = 1e6 + 10, M = 2e6 + 10, mod = 1e9 + 7;



void solve(int group_Id) {
    
}

signed main()
{
#ifdef A_king
    FREOPEN;
#endif
    // int T;read(T);
    int T = 1;
    for (int i = 1;i <= T;i ++) solve(i);
#ifdef A_king
    cerr << "Run Time: " << (double)(clock() - CLOCK) / CLOCKS_PER_SEC * 1000 << " ms" << endl;
#endif
    return 0;
}
/**
* ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
* │Esc│   │ F1│ F2│ F3│ F4│ │ F5│ F6│ F7│ F8│ │ F9│F10│F11│F12│ │P/S│S L│P/B│  ┌┐    ┌┐    ┌┐
* └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘  └┘    └┘    └┘
* ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐ ┌───┬───┬───┬───┐
* │~ `│! 1│@ 2│# 3│$ 4│% 5│^ 6│& 7│* 8│( 9│) 0│_ -│+ =│ BacSp │ │Ins│Hom│PUp│ │N L│ / │ * │ - │
* ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤ ├───┼───┼───┼───┤
* │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{ [│} ]│ \|  │ │Del│End│PDn│ │ 7 │ 8 │ 9 │   │
* ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤ └───┴───┴───┘ ├───┼───┼───┤ + │
* │ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  │               │ 4 │ 5 │ 6 │   │
* ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────────┤     ┌───┐     ├───┼───┼───┼───┤
* │ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│  Shift   │     │ ↑ │     │ 1 │ 2 │ 3 │   │
* ├─────┬──┴─┬─┴──┬┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐ ├───┴───┼───┤ E││
* │ Ctrl│    │Alt │         Space         │ Alt│    │    │Ctrl│ │ ← │ ↓ │ → │ │   0   │ . │←─┘│
* └─────┴────┴────┴───────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘ └───────┴───┴───┘
*/
