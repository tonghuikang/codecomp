#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <map>
#include <algorithm>

using namespace std;

// Implementing the gcd function compatible with C++14 and before
int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

// Function to get all divisors given the prime factorization
vector<int> get_all_divisors_given_prime_factorization(const vector<int>& factors) {
    map<int, int> counter;
    for (int factor : factors) {
        ++counter[factor];
    }
    
    vector<int> divs = {1};
    for (const auto& it : counter) {
        int prime = it.first;
        int count = it.second;
        
        size_t l = divs.size();
        int prime_pow = 1;

        for (int i = 0; i < count; ++i) {
            prime_pow *= prime;
            for (size_t j = 0; j < l; ++j) {
                divs.push_back(divs[j] * prime_pow);
            }
        }
    }
    return divs;
}

// Function to get the largest prime factor for each number up to SIZE_OF_PRIME_ARRAY
vector<int> get_largest_prime_factors(int num) {
    vector<int> largest_prime_factors(num, 1);
    for (int i = 2; i < num; ++i) {
        if (largest_prime_factors[i] > 1) continue;
        for (int j = i; j < num; j += i) {
            largest_prime_factors[j] = i;
        }
    }
    return largest_prime_factors;
}

// Precomputing prime factors
const int SIZE_OF_PRIME_ARRAY = 2*100000 + 10;
vector<int> largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY);

// Function to get prime factors using precomputed largest prime factors
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

int main() {
    int num_of_test_cases;
    cin >> num_of_test_cases;
    
    for (int case_num = 0; case_num < num_of_test_cases; ++case_num) {
        int n;
        cin >> n;
        
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        
        auto factors = get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(n));
        
        int res = 0;
        
        for (int factor : factors) {
            bool flag = true;
            vector<int> diffs;
            for (int i = 0; i < n / factor - 1; ++i) {
                int a = i * factor, b = (i + 1) * factor;
                for (int j = a; j < b; ++j) {
                    if (arr[j] != arr[j + factor]) {
                        diffs.push_back(abs(arr[j] - arr[j + factor]));
                    }
                }
            }
            if (!diffs.empty()) {
                int gcd_result = diffs[0];
                for (int x : diffs) {
                    gcd_result = gcd(gcd_result, x); // Using the gcd function we implemented
                }
                if (gcd_result == 1) {
                    continue;
                }
            }
            
            if (flag) {
                res++;
            }
        }
        
        cout << res << '\n';
    }
    
    return 0;
}