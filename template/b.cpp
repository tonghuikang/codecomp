#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>

const int MAX_SIZE = 2e5 + 10;

int main() {
    int n;
    std::cin >> n;

    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int MX = 2 * n + 10;

    std::vector<int> pref(1, 0);
    for (int v : a) {
        pref.push_back(pref.back() + v);
    }

    pref.insert(pref.end(), MX, pref.back());

    std::bitset<MAX_SIZE> poss;
    poss[1] = 1;

    for (int i = 0; i < n; ++i) {
        poss |= poss << a[i]; 
    }

    std::vector<int> best;
    for (int i = 0; i < MX; ++i) {
        if (poss[i]) {
            best.push_back(pref[i] - i);
        }
    }

    std::cout << *std::max_element(best.begin(), best.end()) + 1 << std::endl;

    return 0;
}