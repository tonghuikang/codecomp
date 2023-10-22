#include <bits/stdc++.h>
using namespace std;

const int SIZE_OF_PRIME_ARRAY = 1e6 + 10;
vector<int> largest_prime_factors(SIZE_OF_PRIME_ARRAY);
vector<int> primes;

vector<int> get_largest_prime_factors(int num) {
    vector<int> largest_prime_factors(num, 1);
    for(int i = 2; i < num; ++i) {
        if(largest_prime_factors[i] > 1) continue;
        for(int j = i; j < num; j += i) {
            largest_prime_factors[j] = i;
        }
    }
    return largest_prime_factors;
}

vector<int> get_prime_factors_with_precomp(int num) {
    if(num == 0) return {};
    vector<int> factors;
    int lf = largest_prime_factors[num];
    while(lf != num) {
        factors.push_back(lf);
        num /= lf;
        lf = largest_prime_factors[num];
    }
    if(num > 1) factors.push_back(num);
    return factors;
}

vector<int> get_all_divisors_given_prime_factorization(vector<int> factors) {
    map<int, int> c;
    for(int factor : factors) {
        c[factor]++;
    }

    vector<int> divs = {1};
    for(auto [prime, count] : c) {
        int prime_pow = 1;
        for(int i = 0; i < count; ++i) {
            prime_pow *= prime;
            int l = divs.size();
            for(int j = 0; j < l; ++j) {
                divs.push_back(divs[j] * prime_pow);
            }
        }
    }
    sort(divs.begin(), divs.end(), greater<int>());
    return divs;
}

vector<int> divisors(int x) {
    return get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(x));
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY);
    for(int i = 2; i < SIZE_OF_PRIME_ARRAY; ++i) {
        if(largest_prime_factors[i] == i) {
            primes.push_back(i);
        }
    }

    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for(int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        map<int, vector<int>> small_to_large;
        map<int, int> divisor_count, cntr;
        set<int> allset;

        for(int num : arr) {
            cntr[num]++;
            allset.insert(num);
        }

        for(auto [k, v] : cntr) {
            for(int divisor : divisors(k)) {
                divisor_count[divisor] += v;
                if(divisor != k) {
                    small_to_large[divisor].push_back(k);
                }
            }
        }

        long long allres = 0;

        for(auto [k, v0] : cntr) {
            int v = v0;
            map<int, int> cur_counts;

            for(int large : small_to_large[k]) {
                v += cntr[large];
            }

            for(int divisor : divisors(k)) {
                cur_counts[divisor] += divisor_count[divisor];
                cur_counts[divisor] -= v;
            }

            for(int divisor : divisors(k)) {
                int deductible = cur_counts[divisor];
                bool flag = false;
                for(int d : divisors(divisor)) {
                    if(allset.find(d) != allset.end()) {
                        flag = true;
                    }
                    cur_counts[d] -= deductible;
                }
                if(flag) {
                    v += deductible;
                }
            }

            int res = n - v;
            allres += 1LL * res * v0;
        }

        cout << (allres / 2) << "\n";
    }

    t += 1

    return 0;
}
