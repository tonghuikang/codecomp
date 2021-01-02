#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,popcnt,abm,mmx,avx,avx2,fma,tune=native")

#include <bits/stdc++.h>
using namespace std;

// for loops
#define REP(i, A, B) for (int i = A; i < B; ++i)   // for i in range(A,B)
#define REPn(i, A, B) for (int i = A; i > B; --i)  // for i in range(A,B,-1)

// scan to variable
#define SCAN_INT(var) scanf("%d", &var);
#define SCAN_LL(var) scanf("%lld", &var);
#define SCAN_ARR(arr, k) \
    REP(i, 1, n + 1)     \
    scanf("%lld", &arr[i]);
// scan matrix (tbc)
// scan string

// fast io
#define FAST                 \
    ios::sync_with_stdio(0); \
    cin.tie(0);

// debug
#define dbg(x) cerr << ">>> " << #x << " = " << x << "\n";

typedef long long LL;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pd;
typedef vector<int> vi;
typedef vector<ll> vll;

// constants
const int M9 = 1e9 + 7;  // 998244353

// reminders
// If the intended result is LL, make sure the first element in the operation is
// LL e.g. instead of `1 << j`, do `1LL << j`

// ---------------------------- template ends here ----------------------------

const int N = 500 * 1000 + 7;
const int P = 60;

int n;
LL arr[N];
LL cnt[P];
LL val[P];

void solve() {
    REP(i, 0, P)
    cnt[i] = 0;
    REP(i, 0, P)
    val[i] = (1LL << i) % M9;

    SCAN_INT(n);
    SCAN_ARR(arr, n);

    REP(i, 1, n + 1) {
        REP(j, 0, P) { cnt[j] += arr[i] >> j & 1; }
    }

    LL ans = 0;
    REP(i, 1, n + 1) {
        LL exp_or = 0;
        LL exp_and = 0;

        REP(j, 0, P) {
            if (arr[i] & (1LL << j)) {
                exp_or += val[j] * n;
                exp_and += val[j] * cnt[j];
            } else {
                exp_or += val[j] * cnt[j];
            }
            // dbg(exp_or);
            // dbg(exp_and);
            exp_and %= M9;
            exp_or %= M9;
        }
        ans = (ans + 1LL * exp_or * exp_and) % M9;
    }
    printf("%lld\n", ans);
}

int main() {
    FAST int total_cases;
    SCAN_INT(total_cases);

    REP(case_num, 0, total_cases) {
        // printf("Case #%d: ", case_num);    // for Google and Facebook
        solve();
    }
    return 0;
}
