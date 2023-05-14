#include <iostream>
#include <vector>
#include <algorithm>

int solve_(int n, const std::vector<int>& arr) {
    int res = 0;
    std::vector<std::pair<int, int>> arr_with_indices(n);

    for (int i = 0; i < n; ++i) {
        arr_with_indices[i] = {arr[i], i};
    }

    std::sort(arr_with_indices.begin(), arr_with_indices.end());

    for (int i = 0; i < n; ++i) {
        int left = 0;
        int right = 0;
        int count = 0;
        for (int j = i; j < n; ++j) {
            right = std::max(right, arr_with_indices[j].second);
            if (right - left == j - i) {
                count += right - left;
                left = right;
            }
        }
        res += count;
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