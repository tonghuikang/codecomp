#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <cmath>

using namespace std;

const int SIZE_OF_PRIME_ARRAY = 1e6 + 10;

vector<int> get_largest_prime_factors(int num) {
    vector<int> largest_prime_factors(num, 1);
    for (int i = 2; i < num; i++) {
        if (largest_prime_factors[i] > 1) continue;
        for (int j = i; j < num; j += i) {
            largest_prime_factors[j] = i;
        }
    }
    return largest_prime_factors;
}

vector<int> largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY);

vector<int> get_prime_factors_with_precomp(int num) {
    if (num == 0) return {};
    vector<int> factors;
    int lf = largest_prime_factors[num];
    while (lf != num) {
        factors.push_back(lf);
        num /= lf;
        lf = largest_prime_factors[num];
    }
    if (num > 1) factors.push_back(num);
    return factors;
}

vector<int> get_all_divisors_given_prime_factorization(vector<int> factors) {
    unordered_map<int, int> counter;
    for (int f : factors) {
        counter[f]++;
    }

    vector<int> divs = {1};
    for (auto& [prime, count] : counter) {
        int l = divs.size();
        int prime_pow = 1;

        for (int i = 0; i < count; i++) {
            prime_pow *= prime;
            for (int j = 0; j < l; j++) {
                divs.push_back(divs[j] * prime_pow);
            }
        }
    }
    sort(divs.rbegin(), divs.rend());
    return divs;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        unordered_map<int, vector<int>> small_to_large;
        unordered_map<int, int> divisor_count, cntr;
        unordered_set<int> allset;

        for (int num : arr) {
            cntr[num]++;
            allset.insert(num);
            for (int divisor : get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(num))) {
                divisor_count[divisor] += cntr[num];
                if (divisor != num) {
                    small_to_large[divisor].push_back(num);
                }
            }
        }

        long long allres = 0;
        for (auto& [k, v] : cntr) {
            int v0 = v;
            unordered_map<int, int> cur_counts;
            for (int large : small_to_large[k]) {
                v += cntr[large];
            }
            for (int divisor : get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(k))) {
                cur_counts[divisor] += divisor_count[divisor];
                cur_counts[divisor] -= v;
            }
            for (int divisor : get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(k))) {
                int deductible = cur_counts[divisor];
                bool flag = false;
                for (int d : get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(divisor))) {
                    if (allset.find(d) != allset.end()) {
                        flag = true;
                    }
                    cur_counts[d] -= deductible;
                }
                if (flag) {
                    v += deductible;
                }
            }
            int res = n - v;
            allres += (long long) res * v0;
        }
        cout << allres / 2 << endl;
    }
    return 0;
}
