#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>
#include <set>
#include <numeric>
#include <unordered_set>

int binary_search(std::function<bool(int)> func, int left, int right) {
    while (left < right) {
        int mid = (left + right) / 2;
        if (func(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

int solve_(const std::vector<int>& arr, int n, int k) {
    std::vector<int> sorted_arr(arr);
    std::sort(sorted_arr.begin(), sorted_arr.end());

    auto func = [&](int target) {
        std::multiset<int> right_pool(sorted_arr.begin(), sorted_arr.begin() + k);
        std::multiset<int> left_pool;

        std::multiset<int> right_excess(sorted_arr.begin() + k, sorted_arr.end());
        std::unordered_multiset<int> left_excess;

        int right_pool_sum = std::accumulate(right_pool.begin(), right_pool.end(), 0);
        int left_pool_sum = 0;

        for (int x : arr) {
            left_pool.insert(x);
            left_pool_sum += x;

            if (right_pool.count(x)) {
                right_pool.erase(right_pool.find(x));
                right_pool_sum -= x;
            } else {
                right_excess.erase(right_excess.find(x));
                if (!right_pool.empty()) {
                    int val = *right_pool.rbegin();
                    right_pool_sum -= val;
                    right_pool.erase(right_pool.find(val));
                    right_excess.insert(val);
                }
            }

            if (left_pool_sum > target) {
                if (right_excess.empty()) {
                    return false;
                }

                int val = *left_pool.rbegin();
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

    return binary_search(func, *std::min_element(sorted_arr.begin(), sorted_arr.end()), std::accumulate(sorted_arr.begin(), sorted_arr.end(), 0));
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
        std::cout << res << '\n';
    }
    return 0;
}