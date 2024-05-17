#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;

// Function for binary search
int binary_search(function<bool(int)> func_, bool first = true, bool target = true, int left = 0, int right = (1 << 31) - 1) {
    auto func = [func_, first, target](int val) {
        if (first ^ target)
            return !func_(val);
        return func_(val);
    };

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (func(mid))
            right = mid;
        else
            left = mid + 1;
    }

    if (first)
        return left;
    else
        return left - 1;
}

int solve_(int n, vector<int>& arr) {
    auto func = [&arr, n](int k) {
        vector<int> counter(22, 0);
        for (int i = 0; i < k; ++i) {
            int num = arr[i];
            for (int q = 0; q < 22; ++q) {
                if (num & (1 << q))
                    counter[q]++;
            }
        }

        vector<int> ref_counter = counter;

        for (int i = k; i < n; ++i) {
            int num = arr[i];
            for (int q = 0; q < 22; ++q) {
                if (num & (1 << q))
                    counter[q]++;
            }
            num = arr[i - k];
            for (int q = 0; q < 22; ++q) {
                if (num & (1 << q))
                    counter[q]--;
            }
            for (int q = 0; q < 22; ++q) {
                if ((counter[q] > 0) != (ref_counter[q] > 0))
                    return false;
            }
        }
        return true;
    };

    return binary_search(func, true, true, 1, n);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    for (int case_num = 0; case_num < t; ++case_num) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        int res = solve_(n, arr);
        cout << res << endl;
    }

    return 0;
}