#include<iostream>
using namespace std;

typedef long long ll;
typedef long double ld;
 
const ll MAX = 5e5+10;
 
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
	for (ll i = 0; i < 60; ++i) {
		C[i] = 0;
	}
	for (ll i = 0; i < k; ++i) {
    	a = A[i];
    	for (ll j = 0; j < 60; ++j){
    		if (a%2 == 1) {
    			C[j] += 1;
    		}
    		a = a/2;
    	};
    };
    
    // for (ll i = 0; i < 60; ++i){
    //     cout << C[i] << " ";
    // }
    // cout << endl;

    
	ll ret = 0;
	for (ll i = 0; i < k; ++i) {
    	OR = 0;
    	AND = 0;
    	a = A[i];
    	for (ll j = 0; j < 60; ++j) {
    		if (a%2 == 1) {
    			AND += C[j] * V[j];
    			OR += k * V[j];
    		} else {
    			OR += C[j] * V[j];
    		}
    		a = a/2;
		}
    	ret += OR * AND;
		// cout << i << " " << k << " " << OR << " " << AND << endl;
		// i++;
		// if (i == k){
		// 	break;
		// }
    	ret = ret%M9;
	};
    return ret%M9;
}
 
int main() {
	for (ll i = 0; i < 60; ++i) {
		V[i] = tmp;
		tmp = (tmp * 2) % M9;
	}

    cin >> N;
    for (ll z = 0; z < N; ++z) {
    	cin >> k;       
		for (ll i = 0; i < k; ++i) cin >> A[i];
    	cout << solve() << endl;
    }
    return 0;
}