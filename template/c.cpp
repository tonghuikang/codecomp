#include <bits/stdc++.h>

#define ll long long
#define lli long long int
#define li long int
#define ld long double
using namespace std;
const lli mod = 1e9 + 7;
const ll LARGE = 1e16;

vector<ll> maxSlidingWindow(vector<ll> nums, int k) {
    deque<ll> dq;
    vector<ll> ans;
    for (ll i=0; i<nums.size(); i++) {
        if (!dq.empty() && dq.front() == i-k) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();
        dq.push_back(i);
        if (i>=k-1) ans.push_back(nums[dq.front()]);
    }
    
    vector<ll> res;
    int n = ans.size();
    
    for (int i = 0; i < k / 2; i++) {
        res.push_back(ans[k - 1]);
    }
    
    for (int i = k - 1; i < n; i++) {
        res.push_back(ans[i]);
    }
    
    for (int i = 0; i < k / 2; i++) {
        res.push_back(ans[n - 1]);
    }
    
    return res;
}

vector<ll> gen_arr(ll a, ll n) {
    a -= 1;
    
    vector<ll> res;
    
    for (ll i = 0; i < n; i++) {
        res.push_back(-LARGE);
    }
    
    for (ll i = 0; i < n; i++) {
        res.push_back(-abs(a - i));
    }
    
    for (ll i = 0; i < n; i++) {
        res.push_back(-LARGE);
    }
    
    return res;
}
    
ll solve()
{
    ll N, M, D;
    cin >> N >> M >> D;
    
    vector<vector<ll>> mrr;
    
    for (ll i = 0; i < M; i++) {
        ll a, b, t;
        cin >> a >> b >> t;
        vector<ll> curr;
        curr.push_back(a);
        curr.push_back(b);
        curr.push_back(t);
        mrr.push_back(curr);
    }
    
    ll res = 0;
    ll a0, b0, t0;
    a0 = mrr[0][0];
    b0 = mrr[0][1];
    t0 = mrr[0][2];
    vector<ll> dp = gen_arr(a0, N);
    res = b0;
    ll prev_t = t0;
    
    for (int i = 1; i < M; i++) {
        int a, b, t;
        a = mrr[i][0];
        b = mrr[i][1];
        t = mrr[i][2];
        res += b;
        
        ll t_diff = t - prev_t;
        ll dist = t_diff * D;
        ll window_size = 2 * dist + 1;
        
        window_size = min(2 * N - 1, window_size);
        dp = maxSlidingWindow(dp, window_size);
        
        vector<ll> new_dp = gen_arr(a, N);
        
        vector<ll> nxt;
        
        for (int i = 0; i < dp.size(); i++) {
            nxt.push_back(dp[i] + new_dp[i]);
        }
        dp = nxt;
        
        prev_t = t;
    }

    return res + *max_element(begin(dp), end(dp));
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << solve();

    return 0;
}