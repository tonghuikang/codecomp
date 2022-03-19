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

LL inp[3];



def solve_(mrr,n,m,d):
    # your solution here

    def gen_arr(a):
        a -= 1
        return [-LARGE]*n + [-abs(a-i) for i in range(n)] + [-LARGE]*n
        
    res = 0
    a0, b0, t0 = mrr[0]
    dp = gen_arr(a0)
    res = b0
    prev_t = t0

    for a,b,t in mrr[1:]:
        log(a,b,t)
        res += b
        t_diff = t - prev_t
        dist = t_diff * d
        window_size = 2*dist + 1

        # log(len(dp), dp, window_size)

        window_size = min(2*n-1, window_size)
        dp = sliding_window_maximum(dp, window_size)

        log(len(dp), dp, window_size)

        new_dp = gen_arr(a)

        assert len(dp) == len(new_dp)

        dp = [a+b for a,b in zip(dp, new_dp)]
        prev_t = t

    return res + max(dp)



void solve() {
    LL n;
    LL m;
    LL d;
    LL a;
    LL b;
    LL t;
    LL res;
    LL prevt;
    LL LARGE;

    LARGE = 10**16;

    inp = SCAN_LL(inp);
    n = inp[0];
    m = inp[1];
    d = inp[2];

    // dp = vi[n*3];
    // new_dp = vi[n*3];

    inp = SCAN_LL(inp);
    a = inp[0];
    b = inp[1];
    t = inp[2];

    vector<ll> generate(vector<ll>& nums, ll a) {
        vector<ll> ans;
        a -= 1
        for (int i=0; i<nums.size(); i++) {
            ans.push_back(LARGE);
        }
        for (int i=0; i<nums.size(); i++) {
            ans.push_back(abs(a-i));
        }
        for (int i=0; i<nums.size(); i++) {
            ans.push_back(LARGE);
        }
        return ans
    }

    vector<ll> maxSlidingWindow(vector<ll>& nums, ll k) {
        deque<ll> dq;
        vector<ll> ans;
        for (ll i=0; i<nums.size(); i++) {
            if (!dq.empty() && dq.front() == i-k) dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i])
                dq.pop_back();
            dq.push_back(i);
            if (i>=k-1) ans.push_back(nums[dq.front()]);
        }
        return ans;
    }

    res = b;
    prevt = t;
    dp = generate(a)

    REP(i, 1, m) {
        inp = SCAN_LL(inp);
        a = inp[0];
        b = inp[1];
        t = inp[2];
        
        res += b;
    }        



    REP(i, 0, P)
    cnt[i] = 0;
    REP(i, 0, P)
    val[i] = (1LL << i) % M9;

    SCAN_INT(n);
    SCAN_ARR(arr, n);

    REP(i, 1, n + 1) {
        REP(j, 0, P) { cnt[j] += arr[i] >> j & 1; }
    }

    // LL ans = 0;
    // REP(i, 1, n + 1) {
    //     LL exp_or = 0;
    //     LL exp_and = 0;

    //     REP(j, 0, P) {
    //         if (arr[i] & (1LL << j)) {
    //             exp_or += val[j] * n;
    //             exp_and += val[j] * cnt[j];
    //         } else {
    //             exp_or += val[j] * cnt[j];
    //         }
    //         // dbg(exp_or);
    //         // dbg(exp_and);
    //         exp_and %= M9;
    //         exp_or %= M9;
    //     }
    //     ans = (ans + 1LL * exp_or * exp_and) % M9;
    // }
    // printf("%lld\n", ans);
}

int main() {
    solve();
    return 0;
}
