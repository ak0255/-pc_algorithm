
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

typedef pair<int, int> PII;
typedef long long ll;

inline int read(void)
{
    register int x = 0;
    register short sgn = 1;
    register char c = getchar();
    while (c < 48 || 57 < c)
    {
        if (c == 45)
            sgn = 0;
        c = getchar();
    }
    while (47 < c && c < 58)
    {
        x = (x << 3) + (x << 1) + c - 48;
        c = getchar();
    }
    return sgn ? x : -x;
}
inline void write(ll x)
{
    if (x < 0)
        putchar('-'), x = -x;
    if (x > 9)
        write(x / 10);
    putchar(x % 10 + '0');
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    return 0;
}