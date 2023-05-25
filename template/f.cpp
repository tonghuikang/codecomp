// GPT-4 rewrite

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <iterator>
#include <limits>

long long binary_search(std::function<bool(long long)> func,
                        long long left = 0,
                        long long right = (1LL << 31) - 1) {
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

long long solve_(const std::vector<int>& arr, int n, int k) {
    std::vector<int> sorted_arr(arr);
    std::sort(sorted_arr.begin(), sorted_arr.end());

    auto func = [&](long long target) {
        std::multiset<int> right_pool(sorted_arr.begin(), sorted_arr.begin() + k);
        std::multiset<int> left_pool;

        std::multiset<int> right_excess(sorted_arr.begin() + k, sorted_arr.end());
        std::multiset<int> left_excess;

        long long right_pool_sum = 0;
        for (int val : right_pool) {
            right_pool_sum += val;
        }

        long long left_pool_sum = 0;

        for (int x : arr) {
            left_pool.insert(x);
            left_pool_sum += x;

            auto it = right_pool.find(x);
            if (it != right_pool.end()) {
                right_pool.erase(it);
                right_pool_sum -= x;
            } else {
                right_excess.erase(right_excess.find(x));
                if (!right_pool.empty()) {
                    int val = *right_pool.rbegin();
                    right_pool.erase(right_pool.find(val));
                    right_pool_sum -= val;
                    right_excess.insert(val);
                }
            }

            if (left_pool_sum > target) {
                if (right_excess.empty()) {
                    return false;
                }

                int val = *left_pool.rbegin();
                left_pool.erase(left_pool.find(val));
                left_pool_sum -= val;
                left_excess.insert(val);

                val = *right_excess.begin();
                right_excess.erase(right_excess.begin());
                right_pool_sum += val;
                right_pool.insert(val);
            }

            if (std::max(left_pool_sum, right_pool_sum) <= target) {
                return true;
            }
        }

        return false;
    };

    return binary_search(func, 0, 1e16);
}

int main() {
    int t;
    std::cin >> t;
    for (int case_num = 0; case_num < t; ++case_num) {
        int n, k;
        std::cin >> n >> k;
        std::vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
        }
        long long res = solve_(arr, n, k);
        std::cout << res << std::endl;
    }

    return 0;
}