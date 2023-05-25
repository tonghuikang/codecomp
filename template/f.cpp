#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,sse4.1,sse4.2,popcnt,abm,mmx,avx,avx2,fma,tune=native")

#include <bits/stdc++.h>
using namespace std;

// for loops
#define REP(i, A, B) for (int i = A; i < B; ++i)   // for i in range(A,B)
#define REPn(i, A, B) for (int i = A; i > B; --i)  // for i in range(A,B,-1)

// scan to variable
#define SCAN_INT(var) scanf("%d", &var);
#define SCAN_LL(var) scanf("%lld", &var);
#define SCAN_ARR(arr, k) \
    REP(i, 1, n + 1)     \
    scanf("%lld", &arr[i]);
// scan matrix (tbc)
// scan string

// fast io
#define FAST                 \
    ios::sync_with_stdio(0); \
    cin.tie(0);

// debug
#define dbg(x) cerr << ">>> " << #x << " = " << x << "\n";


#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>
#include <set>
#include <numeric>
#include <unordered_set>

long long binary_search(std::function<bool(long long)> func, long long left, long long right) {
    while (left < right) {
        long long mid = (left + right) / 2;
        if (func(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

long long solve_(const std::vector<long long>& arr, int n, int k) {
    std::vector<long long> sorted_arr(arr);
    std::sort(sorted_arr.begin(), sorted_arr.end());

    auto func = [&](long long target) {
        std::multiset<long long> right_pool(sorted_arr.begin(), sorted_arr.begin() + k);
        std::multiset<long long> left_pool;

        std::multiset<long long> right_excess(sorted_arr.begin() + k, sorted_arr.end());
        std::unordered_multiset<long long> left_excess;

        long long right_pool_sum = std::accumulate(right_pool.begin(), right_pool.end(), 0LL);
        long long left_pool_sum = 0;

        for (long long x : arr) {
            left_pool.insert(x);
            left_pool_sum += x;

            if (right_pool.count(x)) {
                right_pool.erase(right_pool.find(x));
                right_pool_sum -= x;
            } else {
                right_excess.erase(right_excess.find(x));
                if (!right_pool.empty()) {
                    long long val = *right_pool.rbegin();
                    right_pool_sum -= val;
                    right_pool.erase(right_pool.find(val));
                    right_excess.insert(val);
                }
            }

            if (left_pool_sum > target) {
                if (right_excess.empty()) {
                    return false;
                }

                long long val = *left_pool.rbegin();
                left_pool_sum -= val;
                left_pool.erase(left_pool.find(val));
                left_excess.insert(val);

                val = *right_excess.begin();
                right_pool_sum += val;
                right_excess.erase(right_excess.begin());
                right_pool.insert(val);
            }

            if (std::max(left_pool_sum, right_pool_sum) <= target) {
                return true;
            }
        }

        return false;
    };

    return binary_search(func, *std::min_element(sorted_arr.begin(), sorted_arr.end()), std::accumulate(sorted_arr.begin(), sorted_arr.end(), 0LL));
}

int main() {
    FAST
    int t;
    std::cin >> t;
    for (int case_num = 0; case_num < t; ++case_num) {
        int n, k;
        std::cin >> n >> k;
        std::vector<long long> arr(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
        }
        long long res = solve_(arr, n, k);
        std::cout << res << '\n';
    }
    return 0;
}