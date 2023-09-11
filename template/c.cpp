#include <iostream>
#include <vector>
#include <set>
#include <stdexcept>

int query(int pos) {
    std::cout << pos << std::endl;
    std::cout.flush();
    int response;
    std::cin >> response;
    return response;
}

int main() {
    int t;
    std::cin >> t;
    for (int case_num = 0; case_num < t; ++case_num) {
        int n;
        std::cin >> n;
        std::vector<int> arr(n);
        std::set<int> arrset;
        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i];
            arrset.insert(arr[i]);
        }
        
        int cur = 0;
        while (arrset.count(cur)) {
            ++cur;
        }
        
        while (true) {
            cur = query(cur);
            if (cur == -1) {
                break;
            }
            if (cur == -2) {
                throw std::runtime_error("Assertion failed");
            }
        }
    }
    return 0;
}