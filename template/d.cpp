#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

const int SIZE_OF_PRIME_ARRAY = 1000010;
std::vector<int> largest_prime_factors(SIZE_OF_PRIME_ARRAY);
std::vector<int> primes;

std::vector<int> get_largest_prime_factors(int num) {
    for (int i = 2; i < num; ++i) {
        if (largest_prime_factors[i] > 1)
            continue;
        for (int j = i; j < num; j += i) {
            largest_prime_factors[j] = i;
        }
    }
    return largest_prime_factors;
}

std::vector<int> get_prime_factors_with_precomp(int num) {
    std::vector<int> factors;
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

std::vector<int> get_all_divisors_given_prime_factorization(const std::vector<int>& factors) {
    std::map<int, int> c;
    for (int factor : factors) {
        c[factor]++;
    }
    std::vector<int> divs = {1};
    for (const auto& [prime, count] : c) {
        int l = divs.size();
        int prime_pow = 1;
        for (int i = 0; i < count; ++i) {
            prime_pow *= prime;
            for (int j = 0; j < l; ++j) {
                divs.push_back(divs[j] * prime_pow);
            }
        }
    }
    std::sort(divs.begin(), divs.end(), std::greater<int>());
    return divs;
}

std::vector<int> divisors(int x) {
    return get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(x));
}

int main() {
    largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY);
    for (int i = 2; i < SIZE_OF_PRIME_ARRAY; ++i) {
        if (largest_prime_factors[i] == i) {
            primes.push_back(i);
        }
    }

    int t;
    std::cin >> t;
    while (t--) {
        int n;
        std::cin >> n;
        std::vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
        }

        std::map<int, std::vector<int>> small_to_large;
        std::map<int, int> divisor_count, cntr;

        for (int num : arr) {
            cntr[num]++;
        }

        for (const auto& [k, v] : cntr) {
            for (int divisor : divisors(k)) {
                divisor_count[divisor] += v;
                if (divisor != k) {
                    small_to_large[divisor].push_back(k);
                }
            }
        }

        int allres = 0;
        for (const auto& [k, v] : cntr) {
            int v0 = v;
            std::map<int, int> cur_counts;
            for (int large : small_to_large[k]) {
                v += cntr[large];
            }
            for (int divisor : divisors(k)) {
                cur_counts[divisor] += divisor_count[divisor];
                cur_counts[divisor] -= v;
            }

            for (int divisor : divisors(k)) {
                int deductible = cur_counts[divisor];
                bool flag = false;
                for (int d : divisors(divisor)) {
                    if (cntr.find(d) != cntr.end()) {
                        flag = true;
                    }
                    cur_counts[d] -= deductible;
                }
                if (flag) {
                    v += deductible;
                }
            }

            int res = n - v;
            allres += res * v0;
        }

        std::cout << (allres / 2) << std::endl;
    }
    return 0;
}
