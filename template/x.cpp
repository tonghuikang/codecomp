#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,popcnt,abm,mmx,avx,avx2,fma,tune=native")

#include <bits/stdc++.h>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
#define sz(v) (int)v.size()

#define MOO(i, a, b) for (int i=a; i<b; i++)
#define M00(i, a) for (int i=0; i<a; i++)
#define MOOd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define M00d(i,a) for (int i = (a)-1; i >= 0; i--)

#define FAST ios::sync_with_stdio(0); cin.tie(0);
#define finish(x) return cout << x << '\n', 0;
#define dbg(x) cerr << ">>> " << #x << " = " << x << "\n";

typedef long long LL;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pd;
typedef complex<ld> cd;
typedef vector<int> vi;
typedef vector<ll> vll;

// ll MOD = 1000000007;

const int N = 500 * 1000 + 7;
const int P = 60;
const int MX = 1e9 + 7;

int n;
LL in[N];
int cnt[P];

void solve(){
	scanf("%d", &n);
	for(int i = 0; i < P; ++i)
		cnt[i] = 0;
	
	for(int i = 1; i <= n; ++i){
		scanf("%lld", &in[i]);
		for(int j = 0; j < P; ++j)
			cnt[j] += in[i] >> j & 1;
	}
	
	int ans = 0;
	for(int i = 1; i <= n; ++i){
		LL exp_or = 0, exp_and = 0;
		for(int j = 0; j < P; ++j){
			if(in[i] >> j & 1){
				exp_or += (1LL << j) % MX * n;
				exp_and += (1LL << j) % MX * cnt[j];
			}
			else
				exp_or += (1LL << j) % MX * cnt[j];
		}
		
		exp_and %= MX, exp_or %= MX;
		ans = (ans + 1LL * exp_or * exp_and) % MX;
	}
	
	printf("%d\n", ans);
}

int main(){ FAST
	int cases;
	scanf("%d", &cases);
	
	while(cases--)
		solve();
	return 0;
}
