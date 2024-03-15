#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// ---------------------------- template ends here ----------------------------

int solve_(string srr) {
    // your solution here
    int n = srr.length();

    // brute force, leap over the question marks
    vector<int> arr(n, 0);
    vector<int> jump(n, 0);
    int curjump = 1;
    int non_question_idx = n;

    for (int i = n - 1; i >= 0; i--) {
        arr[i] = non_question_idx;
        jump[i] = curjump;
        if (srr[i] != '?') {
            non_question_idx = i;
            curjump = 1;
        } else {
            curjump++;
        }
    }

    int maxres = 0;

    for (int i = 0; i < n; i++) {
        for (int length = 1; length <= (n - i) / 2; length++) {
            int j = i + length;

            int x = i;
            int y = j;

            while (x < i + length && y < j + length) {
                if (srr[x] != srr[y] && srr[x] != '?' && srr[y] != '?') {
                    break;
                }
                int maxjump = max(jump[x], jump[y]);
                x += maxjump;
                y += maxjump;
            }

            if (x >= i + length && y >= j + length) {
                maxres = max(maxres, length);
            }
        }
    }

    return maxres * 2;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        string srr;
        cin >> srr;

        int res = solve_(srr);
        cout << res << endl;
    }

    return 0;
}