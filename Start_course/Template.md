

# Lucas定理

```cpp
ll quick_pow(ll a, ll n, ll q)
{
    ll ret = 1;
    a %= q;
    while (n)
    {
        if (n & 1)
            ret = ret * a % q;
        a = a * a % q;
        n >>= 1;
    }
    return ret;
}
ll getc(ll n, ll m, ll q)
{
    if (n < m)
        return 0;
    if (m > n - m)
        m = n - m;
    ll s1 = 1, s2 = 1;
    for (int i = 0; i < m; ++i)
    {
        s1 = s1 * (n - i) % q;
        s2 = s2 * (i + 1) % q;
    }
    return s1 * quick_pow(s2, q - 2, q) % q;
}
ll lucas(ll n, ll m, ll q)
{
    if (!m)
        return 1;
    return getc(n % q, m % q, q) * lucas(n / q, m / q, q) % q;
}

```

# min25筛

```cpp
inline ll FUN(ll v, ll N, ll nd, ll nv) { return v >= nd ? (N / v - 1) : (nv - v); }
ll PrimeSum(ll N)
{
    ll *S, *V, r = (ll)sqrt(N);
    ll nd = N / r;
    ll nv = r + nd - 1;
    V = new ll[nv], S = new ll[nv];
    for (ll i = 0; i < r; i++)
        V[i] = N / (i + 1);
    for (ll i = r; i < nv; i++)
        V[i] = V[i - 1] - 1;
    for (ll i = 0; i < nv; i++)
        S[i] = V[i] * (V[i] + 1) / 2 - 1;
    for (ll p = 2; p <= r; p++)
    {
        if (S[nv - p] > S[nv - p + 1])
        {
            ll sp = S[nv - p + 1];
            ll p2 = p * p;
            for (ll i = 0; i < nv; i++)
            {
                if (V[i] >= p2)
                    S[i] -= p * (S[FUN(V[i] / p, N, nd, nv)] - sp);
                else
                    break;
            }
        }
    }
    return S[0];
}
```

# 杜教筛

```cpp
typedef long long ll;
const int mod = 1000000007;
const int maxn = 5000000;
ll pai[maxn + 5];
int prim[maxn + 5], cnt, mu[maxn + 5];
bool vis[maxn + 5];
unordered_map<int, int> ans_mu;
unordered_map<int, ll> ans_pai;
void init()
{
    mu[1] = pai[1] = 1;
    for (int i = 2; i <= maxn; ++i)
    {
        if (!vis[i])
            prim[++cnt] = i, mu[i] = -1, pai[i] = i - 1;
        for (int j = 1; j <= cnt && prim[j] * i <= maxn; ++j)
        {
            vis[prim[j] * i] = 1;
            if (i % prim[j] == 0)
            {
                pai[i * prim[j]] = pai[i] * prim[j];
                break;
            }
            pai[i * prim[j]] = pai[prim[j]] * pai[i];
            mu[i * prim[j]] = -mu[i];
        }
    }
    for (int i = 1; i <= maxn; ++i)
        mu[i] += mu[i - 1], pai[i] += pai[i - 1];
}
//φ前缀和
ll get_pai(ll x)
{
    if (x <= maxn)
        return pai[x];
    if (ans_pai[x])
        return ans_pai[x];
    ll ans = ((1ll + x) * x) / 2ll;
    for (int l = 2, r; l <= x; l = r + 1)
    {
        r = x / (x / l);
        ans -= 1ll * (r - l + 1) * get_pai(x / l);
    }
    return ans_pai[x] = ans;
}
//i * φ前缀和
ll get_piai(ll x)
{
    if (x <= maxn)
        return pai[x];
    if (ans_pai[x])
        return ans_pai[x];
    ll ans = x * (x + 1ll) * (2ll * x + 1ll) / (ll)6;
    for (int l = 2, r; l <= x; l = r + 1)
    {
        r = x / (x / l);
        ans -= 1ll * (r - l + 1) * get_piai(x / l);
    }
    return ans_pai[x] = ans;
}
//μ前缀和
int get_mu(int x)
{
    if (x <= maxn)
        return mu[x];
    if (ans_mu[x])
        return ans_mu[x];
    int ans = 1;
    for (int l = 2, r; l <= x; l = r + 1)
    {
        r = x / (x / l);
        ans -= (r - l + 1) * get_mu(x / l);
    }
    return ans_mu[x] = ans;
}
//i * μ前缀和
int get_miu(int x)
{
    if (x <= maxn)
        return mu[x];
    if (ans_mu[x])
        return ans_mu[x];
    int ans = 1;
    for (int l = 2, r; l <= x; l = r + 1)
    {
        r = x / (x / l);
        ans -= (r - l + 1) * l * get_miu(x / l);
    }
    return ans_mu[x] = ans;
}
void doit()
{
    int T = read();
    while (T--)
    {
        int x = read();
        //TODO:选择要输出的
    }
}

```



# 拓展欧几里得算法

```cpp
int exgcd(int a, int b, int &x, int &y)  // 扩展欧几里得算法, 求x, y，使得ax + by = gcd(a, b)
{
    if (!b)
    {
        x = 1; y = 0;
        return a;
    }
    int d = exgcd(b, a % b, y, x);
    y -= (a / b) * x;
    return d;
}

```

# add - 高精度加法

```cpp
vector<int> add(vector<int> &A, vector<int> &B)  // C = A + B, A >= 0, B >= 0
{
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ )
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}
```

# sub - 高精度减法

```cpp
vector<int> sub(vector<int> &A, vector<int> &B)  // C = A - B, 满足A >= B, A >= 0, B >= 0
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```



# mul - 高精度乘低精度

```cpp
vector<int> mul(vector<int> &A, int b)  // C = A * b, A >= 0, b >= 0
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();

    return C;
}

```



# div - 高精度除以低精度

```cpp
vector<int> div(vector<int> &A, int b, int &r)  // A / b = C ... r, A >= 0, b > 0
{
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}
```

# 欧拉筛质数

```cpp
int st[N], primes[N], cnt;
void ola(int n)
{
    for (int i = 2; i <= n; i++)
    {
        if (st[i] == 0)
            primes[cnt++] = i;                   //将质数存到primes中
        for (int j = 0; primes[j] * i <= n; j++) //要确保质数的第i倍是小于等于n的。
        {
            st[primes[j] * i] = 1;
            if (i % primes[j] == 0)
                break;
        }
    }
}
```

# spfa判断是否有环

```cpp
bool spfa() {
// 如果存在负环，则返回true，否则返回false。
// 不需要初始化dist数组
// 原理：如果某条最短路径上有n个点（除了自己），那么加上自己之后一共有n+1个点，
// 由抽屉原理一定有两个点相同，所以存在环。
    int hh = 0, tt = 0;

    for (int i = 1; i <= n; i ++ ) q[tt ++ ] = i, st[i] = true, dist[i] = cnt[i] = 0;

    while (hh != tt)
    {
        int t = q[hh ++ ];
        if (hh == N) hh = 0;
        st[t] = false;

        for (int i =  h[t]; ~i; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t]  + w[i];
                cnt[j] = cnt[t] + 1;
                if (cnt[j] >= n) return true;
                if (!st[j])
                {
                    st[j] = true;
                    q[tt ++ ] = j;
                    if (tt == N) tt = 0;
                }
            }
        }
    }

    return false;
}
```



# 弗洛伊德求最小环

```cpp
int pos[N][N];  // pos存的是中间点k
int path[N], cnt;  // path 当前最小环的方案, cnt环里面的点的数量

// 递归处理环上节点
void get_path(int i, int j) {
    if (pos[i][j] == 0) return;  // i到j的最短路没有经过其他节点

    int k = pos[i][j];  // 否则,i ~ k ~ j的话,递归处理 i ~ k的部分和k ~ j的部分
    get_path(i, k);
    path[cnt ++] = k;  // k点放进去
    get_path(k, j);
}

void floyd() {// 弗洛伊德求最小环
    int res = 0x7f7f7f7f;

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i < k; i++) {
            for (int j = 1; j < i; j++) {
                if (res > dist[i][j] + d[i][k] + d[k][j]) {
                    res = dist[i][j] + d[i][k] + d[k][j];
                    cnt = 0;
                    path[cnt ++] = k;  // 先把k放进去
                    path[cnt ++] = i;  // 从k走到i(k固定的)
                    get_path(i ,j);  // 递归求i到j的路径
                    path[cnt ++] = j;  // j到k, k固定
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];  
                    pos[i][j] = k;
                }
            }
        }
    }
}
```

# splay树

```cpp
struct Node {
    int s[2], p, v;// 两个儿子、父亲、编号
    int size;// 节点个数
    // TODO: 节点额外属性
    
    void init(int _v, int _p) {
        v = _v, p = _p;
        size = 1;
    }
}tr[N];
int root, idx;// 根节点、插入时的新编号

void pushup(int x) {
    tr[x].size = tr[tr[x].s[0]].size + tr[tr[x].s[1]].size + 1;// 更新子树节点数
    // TODO: 节点信息上传操作
}

void pushdown(int x) {
    // TODO:节点信息下传操作
}

void rotate(int x) {
    int y = tr[x].p, z = tr[y].p;// y是x的父亲，z是y的父亲
    int k = tr[y].s[1] == x;// 如果k为0表示x是y的左儿子，如果k为1表示x是y的右儿子
    tr[z].s[tr[z].s[1] == y] = x, tr[x].p = z;// z的儿子等于x，x的父亲等于z
    tr[y].s[k] = tr[x].s[k ^ 1], tr[tr[x].s[k ^ 1]].p = y;// y的另一个儿子，等于x的一个儿子
    tr[x].s[k ^ 1] = y, tr[y].p = x;// x的一个儿子给了y，那么y就成为x的儿子
    pushup(y), pushup(x);// x、y的子树信息发生改变，又由于y在x下面，所以先维护y、然后维护x
}

void splay(int x, int k) {// 把x翻转到k下面，k == 0表示翻转到根
    while (tr[x].p != k) {// 如果还没翻转到就继续翻
        int y = tr[x].p, z = tr[y].p;
        if (z != k) {// 如果z不等于k，说明x还要持续往上翻
            if ((tr[y].s[1] == x) ^ (tr[z].s[1] == y)) rotate(x);// 如果x和y不是一条链的关系，就先翻x
            else rotate(y);// 如果是一条链，就先翻y
        }
        rotate(x);// 最后翻一下x
    }
    if (!k) root = x;
}

// 序号左小右大
void insert(int v) {
    int u = root, p = 0;
    while (u) p = u, u = tr[u].s[v > tr[u].v];// 如果v > tr[u].v就往右子树递归
    u = ++idx;// 找到v应该放的地方，给他一个新的编号
    if (p) tr[p].s[v > tr[p].v] = u;// 如果有父亲节点，就更新
    tr[u].init(v, p);// 更新这个节点的信息
    splay(u, 0);// 旋转到根
}

// 寻找第k个数的编号
int get_k(int k) {
    int u = root;
    while (true) {
        pushdown(u);
        if (tr[tr[u].s[0]].size >= k) u = tr[u].s[0];
        else if (tr[tr[u].s[0]].size + 1 == k) return u;
        else k -= tr[tr[u].s[0]].size + 1, u = tr[u].s[1];
    }
    return -1;// 如果没找到
}
void output(int u) {
    pushdown(u);
    if (tr[u].s[0]) output(tr[u].s[0]);
    if (tr[u].v >= 1 && tr[u].v <= n) cout << tr[u].v << " ";
    if (tr[u].s[1]) output(tr[u].s[1]);
}
```

# KMP

```cpp
int lenb = b.length()
int lena = a.length()

for (int i = 2, j = 0; i <= lenb; i++)
{
    while (j && b[i] != b[j + 1]) j = ne[j];
    if (b[i] == b[j + 1]) j++;
    ne[i] = j;
}
for (int i = 1, j = 0; i <= lena; i++)
{
    while (j && a[i] != b[j + 1]) j = ne[j];
    if (a[i] == b[j + 1]) j++;
    if (j == lenb)
    {
        cout << i - lenb + 1 << endl;// 如果可以完全匹配，输出第一个字符的位置
        j = ne[j];
    }
}
```

# inv线性求逆元

```cpp
inv[1] = 1;
for(int i = 2;i <= n;i ++)
    inv[i] = (p - p / i) * inv[p % i] % p;
```

# 可持久化求最大异或

```cpp
5 5
2 6 4 3 6
A 1 
Q 3 5 4 
A 4 
Q 5 7 0 
Q 3 6 6 

int tr[M][2], max_id[M];
int s[N];
int root[N], idx;

void insert(int k, int p, int q) {// 第k个、上一个root编号、当前root编号
    max_id[q] = k;
    for (int i = 25;i >= 0;i --) {
        int v = s[k] >> i & 1;
        // 如果前一个root或者往下路径还存在，那么我也可以走你的v ^ 1，当然，如果你的v ^ 1为0，也代表我也走不到v ^ 1
        if (p) tr[q][v ^ 1] = tr[p][v ^ 1];
        tr[q][v] = ++ idx;//! 给当前标号
        max_id[tr[q][v]] = k;// 这条路是从k走来的
        q = tr[q][v], p = tr[p][v];
    }
}

int query(int p, int l, int c) {

    for (int i = 25;i >= 0;i --) {
        int v = c >> i & 1;
        if (max_id[tr[p][v ^ 1]] >= l) p = tr[p][v ^ 1];
        else p = tr[p][v];
    }

    return c ^ s[max_id[p]];
}

signed main()
{
    // ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    // freopen("in.in", "r", stdin);freopen("out.out", "w", stdout);
    cin >> n >> m;
    max_id[0] = -1;
    root[0] = ++ idx;
    insert(0, 0, 1);
    for (int i = 1;i <= n;i ++) {
        int x;
        scanf("%d", &x);
        s[i] = s[i - 1] ^ x;
        root[i] = ++ idx;
        insert(i, root[i - 1], root[i]);
    }
    while (m --) {
        char op[2];
        scanf("%s", op);
        if(*op == 'A')
        {
            int x;
            scanf("%d", &x);
            n ++;
            root[n] = ++ idx;
            s[n] = s[n - 1] ^ x;
            insert(n, root[n - 1], root[n]);
        }
        else
        {
            int l, r, x;
            scanf("%d%d%d", &l, &r, &x);
            printf("%d\n", query(root[r - 1], l - 1, s[n] ^ x));
        }
    }
    return 0;
}
```

# 树链刨分

```cpp
int h[N], e[M], ne[M], idx;
void add(int a, int b) {
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++;
}
int sz[N], big[N], fa[N], top[N], dep[N], L[N], R[N], Node[N], totdfn;
// sz大小，big重儿子，[L-R]子树区间(包含当前根节点)，Node编号为i的节点，res答案数组
void dfs1(int u, int f) {
    fa[u] = f;sz[u] = 1;dep[u] = dep[f] + 1;
    int maxx = -1;
    for (int i = h[u];~i;i = ne[i]) {
        int v = e[i];
        if (v == f) continue;
        dfs1(v, u);
        sz[u] += sz[v];
        if (sz[v] > maxx) {
            maxx = sz[v];
            big[u] = v;
        }
    }
}
void dfs2(int u, int t) {
    L[u] = ++ totdfn;top[u] = t;Node[totdfn] = u;
    if (!big[u]) {
        R[u] = totdfn;
        return ;
    }
    dfs2(big[u], t);// 先遍历轻儿子
    for (int i = h[u];~i;i = ne[i]) {
        int v = e[i];
        if (v == fa[u] || v == big[u]) continue;
        dfs2(v, v);// 轻儿子作为自己的头
    }
    R[u] = totdfn;
}
int lca(int x, int y) {
    while (top[x] != top[y]) {
        if (dep[top[x]] < dep[top[y]]) Swap(x, y);
        x = fa[top[x]];
    }
    return dep[x] < dep[y] ? x : y; 
}
```



# 树上启发式合并

```cpp
int h[N], e[M], ne[M], idx;
int sz[N], big[N], L[N], R[N], Node[N], res[N], totdfn;
// sz大小，big重儿子，[L-R]子树区间(包含当前根节点)，Node编号为i的节点，res答案数组
void add(int a, int b) {
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++;
}
void count(int u, int fa, int val) {
    // TODO: 计算当前根节点的贡献

    for (int i = h[u];~i;i = ne[i]) {
        int v = e[i];
        if (v == fa || v == (val == 1 ? big[u] : -1)) continue;
        // (val == 1 ? big[u] : -1)删除要连带重儿子也删除
        for (int j = L[v];j <= R[v];j ++) {// 对子树进行操作
            int d = Node[j];// 节点d
            // TODO: 计算节点d的贡献

        }
    }
}
int GetRes() {
    // TODO: 答案计算
    return -1;
}
void dfs(int u, int fa) {
    L[u] = ++ totdfn;// 子树区间
    Node[totdfn] = u;
    sz[u] = 1;
    for (int i = h[u];~i;i = ne[i]) {
        int v = e[i];
        if (v == fa) continue;
        dfs(v, u);
        sz[u] += sz[v];
        if (!big[u] || sz[big[u]] < sz[v]) big[u] = v;// 重儿子
    }
    R[u] = totdfn;
}
void dfs(int u, int fa, bool keep) {
    for (int i = h[u];~i;i = ne[i]) {// 计算轻儿子答案
        int v = e[i];
        if(v == fa || v == big[u]) continue;
        dfs(v, u, false);
    }
    if (big[u]) dfs(big[u], u, true);// 保留结果用于继承
    count(u, fa, 1);
    // TODO: 记录答案
    res[u] = GetRes();
    if (keep == false) {
        count(u, fa, -1);
        // TODO: 删除相应参数
    }
}
```



# 差分约束



>   求解不等式组的可行解或者最值

**前提条件：从源点出发可以遍历所有边**

1、可行解

-   根据大小关系建图，例如`v <= u + w`，转换为从u到v有一条长度为w的边

-   从源点跑单源最短路，如果存在负环，无可行解，否则`dist[i]`即为一个可行解

2、最值

-   最小值，通过`v >= u + w`建立从u到v有一条长度为w的边，跑最长路，`dist[i]`即为i的最小值
-   最大值，通过`v <= u + w`建立从u到v有一条长度为w的边，跑最短路，`dist[i]`即为i的最大值

特殊情况`x >= c`，这种情况，应当建立虚拟源点x0，得到`x >= x0 + c`





# $[1-n]$​字典序第k小的数

```cpp
void solve(int group_Id) {
    int n, now = 1;
    read(n);
    auto get = [](int now, ll n) {int steps = 0;ll a = now;ll b = now;while (a <= n) {steps += min(b, n) - a + 1;a = a * 10;b = b * 10 + 9;}return steps;};
    for (int i = 1;i <= 50;i ++) {// 第i小
        int r = i - 1, now = 1;
        while (r) {
            int t = get(now, n);
            if (t <= r) {
                r = r - t;
                now ++;
            }else {
                now *= 10;
                r --;
            }
        }
        cout << now << endl;
    }
}
```



# Template

## default

```cpp
/*
  @file: 0x3f.cpp
  @School: HTU
  @version: c++17
  @copyright: A_king
  @author: A_king
*/
#include <bits/stdc++.h>
using namespace std;
void INIT();
namespace Template {
    #define FREOPEN freopen("in.in", "r", stdin);freopen("out.out", "w", stdout)
    #define out(x...) cout << #x <<" => ";Println(x)
    #define endl '\n'
    #define pb push_back
    #define pf push_front
    #define len(x) (int)(x).size()
    #define all(x) (x).begin(), (x).end()
    #define YES puts("YES")
    #define Yes puts("Yes")
    #define yes puts("yes")
    #define NO puts("NO")
    #define No puts("No")
    #define no puts("no")
    const double PI = acos(-1);const double eps = 1e-6;const int mod = 998244353;const int inf = 0x3f3f3f3f;
    int Mod(int x) {if (x < 0) x += mod;if (x >= mod) x -= mod;return x;}
    template<class T>T ksm(T a, long long b) {T res = 1;while (b) {if (b & 1) res *= a;a *= a;b >>= 1;}return res;}
    struct modint {
        int x;
        modint(int x = 0) : x(Mod(x)) {}
        modint(long long x) : x(Mod(x % mod)) {}
        int val() const {return x;}
        modint operator-() const {return modint(Mod(mod - x));}
        modint inv() const {assert(x != 0);return ksm(*this, mod - 2);}
        modint &operator*=(const modint &T) {x = (long long)(x) * T.x % mod;return *this;}
        modint &operator+=(const modint &T) {x = Mod(x + T.x);return *this;}
        modint &operator-=(const modint &T) {x = Mod(x - T.x);return *this;}
        modint &operator/=(const modint &T) {return *this *= T.inv();}
        friend modint operator*(const modint &T, const modint &Y) {modint res = T;res *= Y;return res;}
        friend modint operator+(const modint &T, const modint &Y) {modint res = T;res += Y;return res;}
        friend modint operator-(const modint &T, const modint &Y) {modint res = T;res -= Y;return res;}
        friend modint operator/(const modint &T, const modint &Y) {modint res = T;res /= Y;return res;}
    };
    typedef modint Z;typedef vector<Z> VZ;typedef vector<VZ> VVZ;typedef long long ll;typedef pair<double, double> PDD;typedef pair<ll, ll> PLL;typedef pair<int, int> PII;typedef pair<int, PII> PIII;typedef vector<int> VI;typedef vector<VI> VVI;typedef vector<ll> VL;typedef vector<VL> VVL;typedef vector<PII> VP;typedef vector<VP> VVP;typedef vector<string> VS;typedef vector<VS> VVS;
    template<typename T> inline T Max(T &a, T b){if (a < b) a = b;return a;}template<typename T> inline T Max(T &a, T b, T c){a = Max(a, b);a = Max(a, c);return a;}
    template<typename T> inline T Min(T &a, T b){if (a > b) a = b;return a;}template<typename T> inline T Min(T &a, T b, T c){a = Min(a, b);a = Min(a, c);return a;}
    template<typename T> inline T Abs(T a){if (a < 0) a = -1 * a;return a;}
    template<typename T>T Gcd(T a, T b){return b ? Gcd(b, a % b) : a;}
    template<typename T> inline void Swap(T &a, T &b){a ^= b ^= a ^= b;}
    template<typename T> inline void read(T &x) {x = 0;short sgn = 1;char c = getchar();while (c < 48 || 57 < c) {if (c == 45) sgn = -1;c = getchar();}while (48 <= c && c <= 57) {x = (x << 3) + (x << 1) + c - 48;c = getchar();}x *= sgn;}
    template<typename T, typename... Args> void read(T &first, Args& ... args) {read(first);read(args...);}
    inline ll read() {ll x = 0;short sgn = 1;char c = getchar();while (c < 48 || 57 < c) {if (c == 45) sgn = -1;c = getchar();}while (48 <= c && c <= 57) {x = (x << 3) + (x << 1) + c - 48;c = getchar();}x *= sgn;return x;}
    template<typename ...U>void Println(U... u) {int last_index = sizeof...(U) - 1, index = 0;auto printer = [last_index, &index]<typename Args>(Args args){if (last_index == index++) cout << args << endl;else cout << args << ", ";};(printer(u), ...);}
}
using namespace Template;



// __builtin_popcount(x); 返回x中1的个数 ^^ 32 - __builtin_clz(x);32位整数的位数 ^^ __builtin_parity(x);1的奇偶，偶为0，奇为1
// accumulate(begin(), end(), start_val); 数组求和
// min_element(begin(), end()); 最小元素的迭代器
// max_element(begin(), end()); 最大元素的迭代器
// minmax_element(begin(), end()); PII类型返回两个迭代器
// nth_element(begin(), begin() + k_th, end(), less<int>()); //下标从begin()开始，默认寻找第k小的数
// priority_queue<type, vector<type>, greater<type>> q; 大根堆，重载大于号
// map<key, value> key -> PII √, unordered_map可能导致二次时间复杂度
// vector find(begin(), end(), val()) rotate(begin(), mid(), end())左循环运动
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

```

## default2

```cpp
/*
  @file: 0x3f.cpp
  @School: HTU
  @version: c++17
  @copyright: A_king
  @author: A_king
*/
#include <bits/stdc++.h>
using namespace std;
#define inf 0x3f3f3f3f

template<typename T> inline void read(T &x) {x = 0;short sgn = 1;char c = getchar();while (c < 48 || 57 < c) {if (c == 45) sgn = -1;c = getchar();}while (48 <= c && c <= 57) {x = (x << 3) + (x << 1) + c - 48;c = getchar();}x *= sgn;}
template<typename T, typename... Args> void read(T &first, Args& ... args) {read(first);read(args...);}

const int N = 1e5 + 10;
typedef long long ll;


signed main()
{
#ifdef A_king
    freopen("in.in", "r", stdin);freopen("out.out", "w", stdout);
#endif
    
    return 0;
}

```

## ST表

```cpp
struct ST {
    int n;
    VVI st;
    VI lg;
    ST (int n, VI arr) : n(n), lg(n + 1), st(n + 1, VI (22)) {
        function<void(void)> Init = [&]() {
            for (int i = 1;i <= n;i ++) st[i][0] = arr[i];
            for (int i = 1; i <= n; i++) lg[i] = lg[i - 1] + (1 << lg[i - 1] == i);
            for (int j = 1;j < lg[n];j ++) {
                for (int i = 1;i + (1 << j) - 1 <= n;i ++) {
                    st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
                }
            }
        };
        Init();
    }
    int query(int l, int r) {
        int k = lg[r - l + 1] - 1;
        return max(st[l][k], st[r - (1 << k) + 1][k]);
    }
};
```

## 树状数组（Binary Indexed Tree/Fenwick Tree）

```cpp
template<typename T>
struct BIT {
    int n;
    vector<T> a;
    BIT(int n) : n(n), a(n + 1) {}
    static constexpr int lowbit(int x) { return x & -x;}
    void update(int pos, T val) {
        for (int i = pos;i <= n;i += lowbit(i)) {a[i] += val;}
    }
    T query(int pos) {
        T res = 0;
        for (int i = pos;i > 0;i -= lowbit(i)) {res += a[i];}
        return res;
    }
    T query(int l, int r) {
        return query(r) - query(l - 1);
    }
};
```

## 线段树（Segment Tree）(加）

```cpp
template<typename T>
struct SegT {
    #define lo (o << 1)
    #define ro (o << 1 | 1)
    #define L(x) tr[(x)].lc
    #define R(x) tr[(x)].rc
    #define V(x) tr[(x)].val
    #define LEN(x) (R(x) - L(x) + 1)
    #define mid(x) (L(x) + R(x) >> 1)
    struct Node {
        T val;
        int lc, rc;
        int lazy;
    };
    const int n;
    vector<Node> tr;
    SegT(int n, vector<T> arr) : n(n), tr((n << 2) + 10) {
        function<void(int, int, int)> build = [&](int o, int l, int r) {
            L(o) = l, R(o) = r, tr[o].lazy = 0;
            if (l == r) {
                V(o) = arr[l];
            }else {
                build(lo, l, mid(o)), build(ro, mid(o) + 1, r);
                pushup(o);
            }
        };
        build(1, 1, n);
    }
    void pushup(int o) {// TODO: 利用左右儿子信息维护当前节点的信息
        V(o) = V(lo) + V(ro);
    }
    void pushdown(int o) {// TODO: 将懒标记下传
        if (tr[o].lazy && L(o) != R(o)) {
            V(lo) = V(lo) + tr[o].lazy * LEN(lo);
            V(ro) = V(ro) + tr[o].lazy * LEN(ro);
            tr[lo].lazy += tr[o].lazy;
            tr[ro].lazy += tr[o].lazy;
            tr[o].lazy = 0;
        }
    }
    void update(int l, int r, T d, int o = 1) {
        if (L(o) >= l && R(o) <= r) {// TODO: 修改区间
            V(o) += LEN(o) * d;
            tr[o].lazy += d;
        }else {
            pushdown(o);
            if (l <= mid(o)) update(l, r, d, lo);
            if (r > mid(o)) update(l, r, d, ro);
            pushup(o);
        }
    }
    T query(int l, int r, int o = 1)
    {
        if (L(o) >= l && R(o) <= r) {// TODO 需要补充返回值
            return V(o);  
        }else {
            pushdown(o);
            T res = 0;
            if (l <= mid(o)) res += query(l, r, lo);
            if (r > mid(o)) res += query(l, r, ro);
            return res;
        }
    }
};
```

## 线段树（Segment Tree）(加&乘）

```cpp
template<typename T>
struct SegT {
    #define lo (o << 1)
    #define ro (o << 1 | 1)
    #define L(x) tr[(x)].lc
    #define R(x) tr[(x)].rc
    #define V(x) tr[(x)].val
    #define LEN(x) (R(x) - L(x) + 1)
    #define mid(x) (L(x) + R(x) >> 1)
    int mod;
    struct Node {
        T val;
        int lc, rc;
        T lazy1, lazy2;
    };
    const int n;
    vector<Node> tr;
    SegT(int n, vector<T> arr, int mod) : n(n), tr((n << 2) + 10), mod(mod) {
        function<void(int, int, int)> build = [&](int o, int l, int r) {
            L(o) = l, R(o) = r, tr[o].lazy2 = 0, tr[o].lazy1 = 1;
            if (l == r) {
                V(o) = arr[l];
            }else {
                build(lo, l, mid(o)), build(ro, mid(o) + 1, r);
                pushup(o);
            }
        };
        build(1, 1, n);
    }
    void pushup(int o) {// TODO: 利用左右儿子信息维护当前节点的信息
        V(o) = (V(lo) + V(ro)) % mod;
    }
    void pushdown(int o) {// TODO: 将懒标记下传
        V(lo) = (V(lo) * tr[o].lazy1 + tr[o].lazy2 * LEN(lo)) % mod;
        V(ro) = (V(ro) * tr[o].lazy1 + tr[o].lazy2 * LEN(ro)) % mod;
        tr[lo].lazy1 = tr[lo].lazy1 * tr[o].lazy1 % mod;
        tr[ro].lazy1 = tr[ro].lazy1 * tr[o].lazy1 % mod;
        tr[lo].lazy2 = (tr[lo].lazy2 * tr[o].lazy1 + tr[o].lazy2) % mod; 
        tr[ro].lazy2 = (tr[ro].lazy2 * tr[o].lazy1 + tr[o].lazy2) % mod; 
        tr[o].lazy2 = 0;
        tr[o].lazy1 = 1;
    }
    void update1(int l, int r, T d, int o = 1) {
        if (L(o) >= l && R(o) <= r) {// TODO: 修改区间
            V(o) = V(o) * d % mod;
            tr[o].lazy1 = tr[o].lazy1 * d % mod;
            tr[o].lazy2 = tr[o].lazy2 * d % mod;
        }else {
            pushdown(o);
            if (l <= mid(o)) update1(l, r, d, lo);
            if (r > mid(o)) update1(l, r, d, ro);
            pushup(o);
        }
    }
    void update2(int l, int r, T d, int o = 1) {
        if (L(o) >= l && R(o) <= r) {// TODO: 修改区间
            V(o) = (V(o) + LEN(o) * d) % mod;
            tr[o].lazy2 = (tr[o].lazy2 + d) % mod;
        }else {
            pushdown(o);
            if (l <= mid(o)) update2(l, r, d, lo);
            if (r > mid(o)) update2(l, r, d, ro);
            pushup(o);
        }
    }
    T query(int l, int r, int o = 1)
    {
        if (L(o) >= l && R(o) <= r) {// TODO 需要补充返回值
            return V(o);  
        }else {
            pushdown(o);
            T res = 0;
            if (l <= mid(o)) res = (res + query(l, r, lo)) % mod;
            if (r > mid(o)) res = (res + query(l, r, ro)) % mod;
            return res;
        }
    }
};
```

## 线性基

```cpp
template<typename T>
struct Linear_base {
    T ba[61], temp[61];
    bool flag = false;
    Linear_base() {
        function<void(void)> Init = [&]() {
            for (int i = 0;i < 60;i ++) {
                ba[i] = temp[i] = 0;
            }
        };
        Init();
    }
    void insert(T x) {
        for (int i = 60;i >= 0; i--)
            if (x & (1ll << i))
                if (!ba[i]) {
                    ba[i] = x;
                    return;
                }
            else x ^= ba[i];
        flag = true;
    }
    bool check(T x) {
        for (int i = 60; i >= 0; i--)
            if (x & (1ll << i))
                if (!ba[i]) return false;
                else x ^= ba[i];
        return true;
    }
    T qmax(T res = 0) {
        for (int i = 60;i >= 0; i--)
            res = max(res, res ^ ba[i]);
        return res;
    }
    T qmin() {
        if (flag) return 0;
        for (int i = 0; i <= 60; i++)
            if (ba[i]) return ba[i];
        return -1;
    }
    T query(T k) {// 数组中可以得到的异或k大
        T res = 0;
        int cnt = 0;
        k -= flag;
        if (!k) return 0;
        for (int i = 0; i <= 60; i++)
        {
            for (int j = i - 1; ~j; j--)
                if (ba[i] & (1ll << j)) ba[i] ^= ba[j];
            if (ba[i]) temp[cnt++] = ba[i];
        }
        if (k >= (1ll << cnt)) return -1;
        for (int i = 0; i < cnt; i++)
            if (k & (1ll << i)) res ^= temp[i];
        return res;
    }
};
```

## AC自动机（出现次数）

```cpp
struct AC {
    int tr[M][26], fail[M], e[M], tot;//字典树 指针 标号
    int cnt[N], val[M];// cnt表示第i个字符串出现的次数
    AC() {
        function<void(void)> Init = [&]() {
            tot = 0;
            for (int i = 0;i < N;i ++) {
                cnt[i] = 0;
            }
            for (int i = 0;i < M;i ++) {
                val[i] = fail[i] = e[i] = 0;
                for (int j = 0;j < 26;j ++) {
                    tr[i][j] = 0;
                }
            }
        };
        Init();
    }
    void insert(char *s, int id){// 字典树插入
        int u = 0;
        for(int i = 1;s[i];i ++){
            if(!tr[u][s[i] - 'a']) tr[u][s[i] - 'a'] = ++ tot;
            u = tr[u][s[i] - 'a'];
        }
        e[u] = id;
    }
    queue<int> q;
    void build(){// 计算fail指针
        for(int i = 0;i < 26;i ++)
            if(tr[0][i]) q.push(tr[0][i]);
        while(q.size()){
            int u = q.front();
            q.pop();
            for(int i = 0; i < 26;i ++){
                if(tr[u][i]){
                    fail[tr[u][i]] = tr[fail[u]][i];
                    q.push(tr[u][i]);
                }else tr[u][i] = tr[fail[u]][i];
            }
        }
    }
    int query(char *t){// 询问每个单词出现次数、返回最大次数
        int u = 0, res = 0;
        for(int i = 1;t[i];i ++){
            u = tr[u][t[i] - 'a'];
            for(int j = u;j;j = fail[j]) val[j] ++;
        }
        for(int i = 1;i <= tot;i ++){
            if(e[i]){
                res = max(res, val[i]);
                cnt[e[i]] = val[i];// 通过标号得到次数
            }
        }
        return res;
    }
};
```

## AC自动机（出现个数）

```cpp
struct AC {
    int tr[N][26], fail[N], e[N], tot;
    AC() {
        function<void(void)> Init = [&]() {
            tot = 0;
            for (int i = 0;i < N;i ++) {
                fail[i] = e[i] = 0;
                for (int j = 0;j < 26;j ++) {
                    tr[i][j] = 0;
                }
            }
        };
        Init();
    }
    void insert(char *s){// 字典树插入
        int u = 0;
        for(int i = 1;s[i];i++){
            if(!tr[u][s[i] - 'a']) tr[u][s[i] - 'a'] = ++tot;
            u = tr[u][s[i] - 'a'];
        }
        e[u]++;
    }
    queue<int> q;
    void build(){// 计算fail指针
        for(int i = 0;i < 26;i++){
            if(tr[0][i]) q.push(tr[0][i]);
        }
        while(q.size()){
            int u = q.front();
            q.pop();
            for(int i = 0;i < 26;i++){
                if(tr[u][i]){
                    fail[tr[u][i]] = tr[fail[u]][i];
                    q.push(tr[u][i]);
                }
                else tr[u][i] = tr[fail[u]][i];
            }
        }
    }
    int query(char *t){// 询问几个单词出现过、当且仅当编号不同
        int u = 0, res = 0;
        for(int i = 1;t[i];i++){
            u = tr[u][t[i] - 'a'];
            for(int j = u;j && ~e[j];j = fail[j]){
                res += e[j];
                e[j] = -1;
            }
        }
        return res;
    }
};
```

## 并查集（DSU）

```cpp
struct DSU {
    int n;
    vector<int> fa;
    vector<int> sz;
    DSU(int n) : n(n), fa(n + 1), sz(n + 1) {
        for (int i = 1;i <= n;i ++) {
            fa[i] = i;
            sz[i] = 1;
        }
    }
    int find(int x) {
        return x == fa[x] ? x : fa[x] = find(fa[x]);
    }
    void merge(int a, int b) {
        a = find(a), b = find(b);
        if (sz[a] > sz[b]) swap(a, b);
        fa[a] = b;
        sz[b] += sz[a];
    }
    bool test(int a, int b) {return find(a) == find(b);}
};
```

## 最近公共祖先（distance）

```cpp
struct LCA {
    int root;
    int fa[N][20], dist[N][20], dep[N];
    LCA(int root) : root(root) {
        function<void(void)> Init = [&]() {
            for (int i = 0;i < N;i ++) {
                dep[i] = 0;
                for (int j = 0;j < 20;j ++) {
                    fa[i][j] = dist[i][j] = 0;
                }
            }
        };
        function<void(int, int)> dfs = [&](int u, int father) {
            fa[u][0] = father;
            dep[u] = dep[fa[u][0]] + 1;
            for (int i = 1;i < 20;i ++) {
                fa[u][i] = fa[fa[u][i - 1]][i - 1];
                dist[u][i] = dist[u][i - 1] + dist[fa[u][i - 1]][i - 1];
            }
            for (int i = h[u];~i;i = ne[i]) {
                int j = e[i];
                if (j == father) continue;
                dist[j][0] = w[i];
                dfs(j, u);
            }
        };
        Init();
        dfs(root, root);
    }
    int lca (int x, int y) {
        int res = 0;
        if(dep[x] > dep[y]) swap(x, y);
        int tmp = dep[y] - dep[x];
        for (int j = 0;tmp;j ++, tmp >>= 1) {
            if(tmp & 1) res += dist[y][j], y = fa[y][j];
        }
        if (x == y) return res;
        for (int i = 19;i >= 0;i --) {
            if (fa[x][i] != fa[y][i]) {
                res += dist[x][i] + dist[y][i];
                x = fa[x][i];
                y = fa[y][i];
            }
        }
        res += dist[x][0] + dist[y][0];
        return res;
    }
};

```

## 最近公共祖先（点）

```cpp
struct LCA {
    //fa[u][i]表示u的第2^i个祖先,dep[u]表示u的深度
    int root;
    int fa[N][20], dep[N];
    LCA(int root) : root(root) {
        function<void(void)> Init = [&]() {
            for (int i = 0;i < N;i ++) {
                dep[i] = 0;
                for (int j = 0;j < 20;j ++) {
                    fa[i][j] = 0;
                }
            }
        };
        function<void(int, int)> dfs = [&](int u, int father) {
            fa[u][0] = father;//当前点的第2^0个祖先就是我的父亲
            dep[u] = dep[fa[u][0]] + 1;//当前点的深度就是父亲的深度 + 1
            for (int i = 1;i < 20;i ++) {
                fa[u][i] = fa[fa[u][i - 1]][i - 1];//u的第2^i个祖先,就是第2^(i - 1)个祖先的第2^(i - 1)个祖先
            }
            for (int i = h[u];~i;i = ne[i]) {//遍历子节点
                int j = e[i];
                if (j == father) continue;
                dfs(j, u);
            }
        };
        Init();
        dfs(root, root);
    }
    int lca (int x, int y) {
        if(dep[x] > dep[y]) swap(x, y);//令y为深度大的点
        int tmp = dep[y] - dep[x];//得到深度差
        for (int j = 0;tmp;j ++, tmp >>= 1) {//二进制递减深度
            if(tmp & 1) y = fa[y][j];
        }
        if (x == y) return x;
        //如果不在一个小子树上,继续往上找
        for (int i = 19;i >= 0;i --) {//这里从上往下，使得x和y到距离最近公共祖先最近的点
            if (fa[x][i] != fa[y][i]) {
                x = fa[x][i];
                y = fa[y][i];
            }
        }
        return fa[x][0];
    }
};
```

## Manacher（长度）

```cpp
struct Man {
    int n;
    string str, nstr;
    int lens[2 * N];
    Man(int n) : n(n) {
        function<void(void)> Init = [&]() {
            str = nstr = "";
            for (itn i = 0;i < 2 * n + 5;i ++) {
                len[i] = 0;
            }
        };
        Init();
    }
    void init()//返回字符串长度、str为字符串、nstr为新字符串
    {
        int j = 2;
        nstr += '@', nstr += '#';
        for (int i = 0; i < str.length(); i++)
        {
            nstr += str[i];
            nstr += '#';
        }
        nstr += '*';
    }
    int man()//返回最长字符串、len为字符串长度
    {
        int mx = 0, id = 1, max_len = 0;
        for (int i = 1; i < nstr.length(); i++)
        {
            lens[i] = i < mx ? min(mx - i, lens[2 * id - i]) : 1;
            while (nstr[i + lens[i]] == nstr[i - lens[i]]) lens[i]++;
            if (lens[i] + i > mx)
            {
                mx = lens[i] + i;
                id = i;
            }
            max_len = max(max_len, lens[i]);
        }
        return max_len - 1;
    }
};
```

## Manacher（子串）

```cpp
struct Man {
    int n;
    string str, nstr;
    int lens[2 * N];
    Man(int n) : n(n) {
        function<void(void)> Init = [&]() {
            str = nstr = "";
            for (itn i = 0;i < 2 * n + 5;i ++) {
                len[i] = 0;
            }
        };
        Init();
    }
    void init()//str为字符串、nstr为新字符串
    {
        int j = 2;
        nstr += '@', nstr += '#';
        for (int i = 0; i < str.length(); i++)
        {
            nstr += str[i];
            nstr += '#';
        }
        nstr += '*';
    }
    string man() {//返回最长字符子串、len为字符串长度
        int mx = 0, id = 1, max_len = 0, startx = 2, lenx = 1;
        for (int i = 1; i < nstr.length(); i++)
        {
            lens[i] = i < mx ? min(mx - i, lens[2 * id - i]) : 1;
            while (nstr[i + lens[i]] == nstr[i - lens[i]]) lens[i]++;
            if(lens[i] > max_len){
                    startx = i;
                    lenx = lens[i];
                }
            if (lens[i] + i > mx)
            {
                mx = lens[i] + i;
                id = i;
            }
            max_len = max(max_len, lens[i]);
        }
        nstr = nstr.substr(startx, lenx);
        if((max_len - 1) & 1){
            string str = nstr.substr(1);
            reverse(str.begin(), str.end());
            nstr = str + nstr;
        }else{
            reverse(nstr.begin(), nstr.end());
            string str = nstr;
            reverse(nstr.begin(), nstr.end());
            nstr = str + nstr;
        }
        string cc = "";
        for(int i = 0;i < nstr.length();i++){
            if(nstr[i] != '#') cc += nstr[i];
        }
        return cc;
    }
};
```

## Tarjan（强连通分量）

```cpp
struct Tarjan {
    int n;
    int dfn[N], low[N], sta[N], gro[N], tot[N];
    bool instack[N];//是否在栈内
    int stop, bcnt, dindex;//stop栈内元素个数,bcnt为分组的组号,dindex为时间戳
    Tarjan(int n) : n(n) {
        function<void(void)> Init = [&]() {
            stop = bcnt = dindex = 0;
            for (int i = 0;i <= n;i ++) {
                dfn[i] = low[i] = sta[i] = gro[i] = tot[i] = 0;
                instack[i] = false;
            }
        };
        Init();
    }
    void tarjan(int u) {
        dfn[u] = low[u] = ++ dindex;//初始都为时间戳
        instack[u] = true;//加入栈内
        sta[++ stop] = u;
        // out(stop);
        for (int i = h[u];~i;i = ne[i]) {
            int j = e[i];
            if (!dfn[j]){
                tarjan(j);
                if (low[j] < low[u]) low[u] = low[j];
            }else if (instack[j] && dfn[j] < low[u]) low[u] = dfn[j];
        }
        if (dfn[u] == low[u]) {
            bcnt ++;
            int j;
            do {
                j = sta[stop--];
                instack[j] = false;
                gro[j] = bcnt;
                tot[bcnt] ++;
            }while (j != u);
        }
    }
};
```

## Tarjan（割边）

```cpp
struct Tarjan {
    int n;
    int dfn[N], low[N], father[N];//dfn(u)为节点u搜索的次序编号(时间戳),low(u)为u或u的子树能够追溯到的最早的栈中节点的次序号
    int dfs_clock, cnt_bridge;//dfs_clock时间戳、cnt_bridge割边数量
    bool isbridge[N];//是否是割边
    vector<PII> res;// 割边集合
    Tarjan(int n) : n(n) {
        function<void(void)> Init = [&]() {
            res.clear();
            dfs_clock = cnt_bridge = 0;
            for (int i = 0;i <= n;i ++) {
                dfn[i] = low[i] = father[i] = 0;
                isbridge[i] = false;
            }
        };
        Init();
    }
    void tarjan(int u, int fa) {
        father[u] = fa;//父亲节点
        low[u] = dfn[u] = ++ dfs_clock;
        for (int i = h[u];~i;i = ne[i]) {
            int v = e[i];
            if (!dfn[v]) {
                tarjan(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > dfn[u]) {
                    isbridge[v] = true;// 如果isbridge为真表示father[v] -> v为一条割边
                    res.push_back({father[v], v});
                    ++ cnt_bridge;
                }
            } else if (dfn[v] < dfn[u] && v != fa) {
                low[u] = min(low[u], dfn[v]);
            }
        }
    }
};
```

## Tarjan（割点）

```cpp
struct Tarjan {
    //dfn(u)为节点u搜索的次序编号(时间戳),low(u)为u或u的子树能够追溯到的最早的栈中节点的次序号
    int n;
    int dfn[N], low[N], cut[N];
    int stop, bcnt, dindex;//dindex为时间戳
    Tarjan(int n) : n(n) {
        function<void(void)> Init = [&]() {
            stop = bcnt = dindex = 0;
            for (int i = 0;i <= n;i ++) {
                dfn[i] = low[i] = cut[i] = 0;
            }
        };
        Init();
    }
    void tarjan(int u, int fa) {
        dfn[u] = low[u] = ++ dindex;//初始都为时间戳
        int child = 0;

        for (int i = h[u];~i;i = ne[i]) {
            int j = e[i];
            if (!dfn[j]){
                tarjan(j, fa);
                low[u] = min(low[u], low[j]);
                if (low[j] >= dfn[u] && u != fa)
                    cut[u] = 1;
                if(u == fa)
                    child ++;
            }else if (j != u) low[u] = min (low[u], dfn[j]);
        }
        if (child >= 2 && u == fa)
            cut[u] = 1;
    }
};
```

### 割点求删除一个点得到最多连通块

```cpp
void tarjan(int u, int fa) {
    dfn[u] = low[u] = ++ dindex;//初始都为时间戳
    int child = 0;
    for (int i = h[u];~i;i = ne[i]) {
        int j = e[i];
        if (!dfn[j]){
            tarjan(j, fa);
            low[u] = min(low[u], low[j]);
            if (low[j] >= dfn[u]) {
                // low比dfn序大，证明j无法回到u，故可以删去u使得j所在连通块被分离出去
                child ++;
            }
        }else low[u] = min (low[u], dfn[j]);
    }
    if (u != fa) child ++;// 如果不是根节点，显然可以使得上方连通块也被分离
    res = Max(res, child);
}
// 最终图中删去一个点可以得到的最多连通块为：图中原有的连通块数量 + res - 1;
```



## splay一套

```cpp
struct splay_tree
{
    int p, son[2], v, cnt, size;
    void init(int _v, int _p)
    {
        v = _v, p = _p;
        size = 1, cnt = 1;
    }
} tr[N];
int root, idx, tag;
void pushup(int x)
{
    tr[x].size = tr[tr[x].son[0]].size + tr[tr[x].son[1]].size + tr[x].cnt;
}
void rotate(int x)
{
    int y = tr[x].p, z = tr[y].p;
    int k = (tr[y].son[1] == x);
    tr[z].son[tr[z].son[1] == y] = x, tr[x].p = z;
    tr[y].son[k] = tr[x].son[k ^ 1], tr[tr[x].son[k ^ 1]].p = y;
    tr[x].son[k ^ 1] = y, tr[y].p = x;
    pushup(y), pushup(x);
}
void splay(int x, int p)
{
    while (tr[x].p != p)
    {
        int y = tr[x].p, z = tr[y].p;
        if (z != p)
        {
            if ((tr[y].son[1] == x) ^ (tr[z].son[1] == y))
                rotate(x);
            else
                rotate(y);
        }
        rotate(x);
    }
    if (!p)
        root = x;
}
void Insert(int x)
{
    int u = root, p = 0;
    while (u)
    {
        if (tr[u].v == x)
        {
            tr[u].cnt++;
            pushup(u);
            splay(u, 0);
            goto next_;
        }
        p = u, u = tr[u].son[x > tr[u].v];
    }
    u = ++idx;
    if (p)
        tr[p].son[x > tr[p].v] = u;
    tr[u].init(x, p);
    splay(u, 0);
next_:;
}
void Remove(int x)
{
    int u = root, p = 0;
    int k;
    while (u)
    {
        if (tr[u].v == x)
            break;
        p = u, u = tr[u].son[x > tr[u].v];
        k = (x > tr[p].v);
    }
    if (!u)
        return;
    else if (tr[u].cnt == 1)
    {
        if (!tr[u].son[0] && !tr[u].son[1])
            tr[p].son[k] = 0, tr[u].p = 0, pushup(p), splay(p, 0);
        else if (!tr[u].son[1])
            tr[p].son[k] = tr[u].son[0], tr[tr[u].son[0]].p = p, tr[u].p = 0, pushup(p), splay(p, 0);
        else if (!tr[u].son[0])
            tr[p].son[k] = tr[u].son[1], tr[tr[u].son[1]].p = p, tr[u].p = 0, pushup(p), splay(p, 0);
        else
        {
            int l = tr[u].son[0], r = tr[u].son[1];
            while (tr[l].son[1])
                l = tr[l].son[1];
            while (tr[r].son[0])
                r = tr[r].son[0];
            splay(l, 0), splay(r, root);
            tr[r].son[0] = 0, tr[tr[r].son[0]].p = 0, pushup(r), pushup(root);
        }
    }
    else
        tr[u].cnt--, pushup(u), splay(u, 0);
}
int get_rank(int p, int x)
{
    if (p == 0)
        return -1;
    else if (x == tr[p].v)
    {
        tag = p;
        return tr[tr[p].son[0]].size + 1;
    }
    else if (x < tr[p].v)
        return get_rank(tr[p].son[0], x);
    else
        return get_rank(tr[p].son[1], x) + tr[tr[p].son[0]].size + tr[p].cnt;
}
int find_rank(int p, int x)
{
    if (p == 0)
        return INF;
    if (tr[tr[p].son[0]].size >= x)
        return find_rank(tr[p].son[0], x);
    if (tr[tr[p].son[0]].size + tr[p].cnt >= x)
    {
        tag = p;
        return tr[p].v;
    }
    return find_rank(tr[p].son[1], x - tr[tr[p].son[0]].size - tr[p].cnt);
}
int get_pre(int x)
{
    int ans = 1;
    int u = root, p = 0;
    while (u)
    {
        if (tr[u].v == x)
            break;
        p = u, u = tr[u].son[x > tr[u].v];
        if (tr[p].v < x && tr[p].v > tr[ans].v)
            ans = p;
    }
    if (!u || !tr[u].son[0])
        return tr[ans].v;
    u = tr[u].son[0];
    while (tr[u].son[1])
        u = tr[u].son[1];
    return tr[u].v;
}
int get_next(int x)
{
    int ans = 2;
    int u = root, p = 0;
    while (u)
    {
        if (tr[u].v == x)
            break;
        p = u, u = tr[u].son[x > tr[u].v];
        if (tr[p].v > x && tr[p].v < tr[ans].v)
            ans = p;
    }
    if (!u || !tr[u].son[1])
        return tr[ans].v;
    u = tr[u].son[1];
    while (tr[u].son[0])
        u = tr[u].son[0];
    return tr[u].v;
}
```

