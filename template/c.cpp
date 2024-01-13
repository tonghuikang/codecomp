#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <numeric>

using namespace std;

const int SIZE_OF_PRIME_ARRAY = 1000006;
vector<int> largest_prime_factors(SIZE_OF_PRIME_ARRAY);

void get_largest_prime_factors() {
    fill(largest_prime_factors.begin(), largest_prime_factors.end(), 1);
    for (int i = 2; i < SIZE_OF_PRIME_ARRAY; ++i) {
        if (largest_prime_factors[i] > 1) continue;
        for (int j = i; j < SIZE_OF_PRIME_ARRAY; j += i) {
            largest_prime_factors[j] = i;
        }
    }
}

vector<int> get_prime_factors_with_precomp(int num) {
    vector<int> factors;
    int lf = largest_prime_factors[num];
    while (lf != num) {
        factors.push_back(lf);
        num /= lf;
        lf = largest_prime_factors[num];
    }
    if (num > 1) {
        factors.push_back(num);
    }
    return factors;
}

vector<int> get_all_divisors_given_prime_factorization(const vector<int>& factors) {
    unordered_map<int, int> count_map;
    for (int factor : factors) {
        count_map[factor]++;
    }

    vector<int> divs = {1};
    for (const auto& [prime, count] : count_map) {
        int l = divs.size(), prime_pow = 1;
        for (int i = 0; i < count; ++i) {
            prime_pow *= prime;
            for (int j = 0; j < l; ++j) {
                divs.push_back(divs[j] * prime_pow);
            }
        }
    }

    return divs;
}

int solve_(int n, const vector<int>& arr) {
    vector<int> factors = get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(n));

    int res = 0;
    for (int factor : factors) {
        vector<int> diffs;
        for (int i = 0; i < n / factor - 1; ++i) {
            int a = i * factor, b = (i + 1) * factor;
            for (int j = 0; j < factor; ++j) {
                if (arr[a + j] != arr[b + j]) {
                    diffs.push_back(abs(arr[a + j] - arr[b + j]));
                }
            }
        }
        
        // No need for a flag, directly use the condition to continue or increment res
        if (!diffs.empty()) {
            int gcd = diffs[0];
            for (int x : diffs) {
                gcd = std::gcd(gcd, x);
            }
            if (gcd != 1) {
                // The condition is met, so we increment res
                res += 1;
            }
        }
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    get_largest_prime_factors();

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int& val : arr) {
            cin >> val;
        }

        int res = solve_(n, arr);
        cout << res << '\n';
    }
    return 0;
}