// learning C++ with https://codeforces.com/contest/1535/submission/118436531
#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,popcnt,abm,mmx,avx,avx2,fma,tune=native")

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pl;
typedef tuple<ll, ll, ll> tl;
typedef tuple<ll, ll, ll, ll> ql;
 
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;

// ---------------------------- template ends here ----------------------------
ll Q, A[300005], C[300005], P[300005][20], V[300005], W[300005];


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
    cin >> Q >> A[0] >> C[0];

    for (ll b = 0; b < 20; b++){
        P[0][b] = -1;
    }

    for (ll q = 1; q <= Q; q++){
        ll t;
        cin >> t;

        if (t == 1){
            cin >> P[q][0] >> A[q] >> C[q];

            for (ll b = 1; b < 20; b++){
                if (P[q][b-1] == -1) {
                    P[q][b] = -1;
                } else {
                    P[q][b] = P[P[q][b - 1]][b - 1];
                    // P[q][b] = P[P[q][0]][b];
                }
            }

        } else {  // t == 2
            cin >> V[q] >> W[q];
            ll lower = 0;
            ll upper = 300005;
            ll x = 0;

			while (lower <= upper) {
				ll test = (lower + upper) / 2;
				ll v = V[q];
				for (ll b = 0; b < 20; b++) {
					if (test & (1ll << b)) {
						v = P[v][b];
						if (v == -1) break;
					}
				}
				if (v == -1 || A[v] == 0) {
					upper = test - 1;
				} else {
					lower = test + 1;
					x = max(x, test);
				}
			}
			
			ll total_gold = 0;
			ll total_cost = 0;
			
			for (ll p = x; p >= 0; p--) {
				ll v = V[q];
				for (ll b = 0; b < 20; b++) {
					if (p & (1ll << b)) {
						v = P[v][b];
					}
				}
				ll buy = min(A[v], W[q] - total_gold);
				total_gold += buy;
				total_cost += buy * C[v];
				A[v] -= buy;
				if (total_gold == W[q]) break;
			}
			
			cout << total_gold << " " << total_cost << endl;
        }

    }



    return 0;
}
