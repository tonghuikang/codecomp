#include <algorithm>
#include <functional>
#include <iostream>
#include <set>
#include <vector>

int binary_search(std::function<bool(int)> func, bool first = true, bool target = true,
                  int left = 0, int right = (1 << 31) - 1) {
    auto func_wrapper = [&](int val) {
        if (first ^ target) {
            return !func(val);
        }
        return func(val);
    };

    while (left < right) {
        int mid = (left + right) / 2;
        if (func_wrapper(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    if (first) {
        return left;
    } else {
        return left - 1;
    }
}

int solve_(const std::vector<int>& arr, int n, int k) {
    std::vector<int> sorted_arr(arr);
    std::sort(sorted_arr.begin(), sorted_arr.end());

    auto func = [&](int64_t target) {
        std::multiset<int> right_pool(sorted_arr.begin(), sorted_arr.begin() + k);
        std::multiset<int> left_pool;

        std::multiset<int> right_excess(sorted_arr.begin() + k, sorted_arr.end());
        std::multiset<int> left_excess;

        int64_t right_pool_sum = 0;
        for (int val : right_pool) {
            right_pool_sum += val;
        }
        int64_t left_pool_sum = 0;

        for (int x : arr) {
            left_pool.insert(x);
            left_pool_sum += x;

            if (right_pool.count(x) > 0) {
                right_pool.erase(right_pool.find(x));
                right_pool_sum -= x;
            } else {
                right_excess.erase(right_excess.find(x));

                if (!right_pool.empty()) {
                    int val = *right_pool.rbegin();
                    right_pool_sum -= val;
                    right_excess.insert(val);
                    right_pool.erase(right_pool.find(val));
                }
            }

            if (left_pool_sum > target) {
                if (right_excess.empty()) {
                    return false;
                }

                int val = *left_pool.rbegin();
                left_pool_sum -= val;
                left_excess.insert(val);
                left_pool.erase(left_pool.find(val));

                val = *right_excess.begin();
                right_pool_sum += val;
                right_pool.insert(val);
                right_excess.erase(right_excess.begin());
            }

            if (std::max(left_pool_sum, right_pool_sum) <= target) {
                return true;
            }
        }

        return false;
    };

    return binary_search(func, true, true, 0, 1e16);
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
        int res = solve_(arr, n, k);
        std::cout << res << std::endl;
    }
}