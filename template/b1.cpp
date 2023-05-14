#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

int solve_(int n, const std::vector<int>& arr_original) {
    int res = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            std::vector<int> arr(arr_original.begin() + i, arr_original.begin() + j);

            std::unordered_map<int, int> pos;
            for (int k = 0; k < arr.size(); ++k) {
                pos[arr[k]] = k;
            }

            std::vector<int> brr = arr;
            std::sort(brr.begin(), brr.end());

            std::vector<int> crr;
            for (int x : brr) {
                crr.push_back(pos[x]);
            }

            int left = 0;
            int right = 0;
            int count = 0;
            for (int k = 0; k < crr.size(); ++k) {
                right = std::max(right, crr[k]);
                if (right == k) {
                    if (right > left) {
                        count += right - left;
                    }
                    left = k + 1;
                }
            }

            res += count;
        }
    }

    return res;
}

int main() {
    int num_cases;
    std::cin >> num_cases;

    for (int case_num = 0; case_num < num_cases; ++case_num) {
        int n;
        std::cin >> n;

        std::vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
        }

        int res = solve_(n, arr);
        std::cout << res << std::endl;
    }

    return 0;
}