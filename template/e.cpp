#include<iostream>
using namespace std;

int i;
int n;

typedef long long ll;
typedef long double ld;
 
const int MAX = 5e5+10;
 
ll N;
ll k;
ll a;

ll OR;
ll AND;

ll A[MAX];
ll C[60];
ll V[60];

ll tmp = 1;
ll M9 = 1000000000 + 7;

ll solve() {
	for (ll i = 0; i < k; ++i) {
    	a = A[i];
    	for (ll j = 0; j < 60; ++i){
    		if (a%2) {
    			C[j] += 1;
    		}
    		a = a/2;
    	};
    };
    
	ll ret = 0;
	for (ll i = 0; i < k; ++i) {
    	OR = 0;
    	AND = 0;
    	a = A[i];
    	for (ll j = 0; j < 60; ++j) {
    		if (a%2) {
    			AND += C[j] * V[j];
    			OR += N * V[j];
    		} else {
    			OR += C[j] * V[j];
    		}
    		a = a/2;
    	ret += OR * AND;
    	ret = ret%M9;
    	};
	};
    return ret;
}
 
int main() {
	for (ll i = 0; i < 60; ++i) {
		V[i] = tmp;
		tmp = (tmp * 2) % M9;
	}
    cin >> N;
    for (ll z = 0; i < N; ++z) {
    	cin >> k;
		for (ll i = 0; i < N; ++i) cin >> A[i];
    	cout << solve();
    }
    return 0;
}