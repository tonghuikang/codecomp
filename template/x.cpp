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

// for loops
#define REP(i, A, B) for (int i=A; i<B; ++i)  // for i in range(A,B)
// #define REPs(i, a, s) for (int i=s; i<(a); ++i)
#define MOO(i, a, b) for (int i=a; i<b; i++)
#define MOOd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define M00d(i,a) for (int i = (a)-1; i >= 0; i--)

// initialise arrays and set default variables - ?

// scan to variable
// list
// matrix

// fast sync
#define FAST ios::sync_with_stdio(0); cin.tie(0);

// debug
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

// reminders
// `1LL << j` remember the LL if you define integers larger than ...

// ll MOD = 1000000007;

const int N = 500 * 1000 + 7;
const int P = 60;
const int M9 = 1e9 + 7;  // 998244353

int n;
LL in[N];
int cnt[P];
int val[P];

void solve(){
	REP(i, 0, P) cnt[i] = 0;
	REP(i, 0, P) val[i] = (1LL << i) % M9;

	scanf("%d", &n);	
	REP(i, 1, n+1){
		scanf("%lld", &in[i]);
    REP(j, 0, P){
      cnt[j] += in[i] >> j & 1;
    }
	}
	
	int ans = 0;
  REP(i, 1, n+1){
		LL exp_or = 0, exp_and = 0;
    REP(j, 0, P){
			if(in[i] & (1LL << j)){
				exp_or += (1LL << j) % M9 * n;
				exp_and += (1LL << j) % M9 * cnt[j];
			}
			else
				exp_or += (1LL << j) % M9 * cnt[j];
		}
		
		exp_and %= M9;
    exp_or %= M9;
		ans = (ans + 1LL * exp_or * exp_and) % M9;
	}
	
	printf("%d\n", ans);
}

int main(){ FAST
	int total_cases;
	scanf("%d", &total_cases);
	
	REP(case_num, 0, total_cases){
    // printf("Case #%d: ", case_num);  // for Google and Facebook
    solve();
  }
	return 0;
}
