#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
using namespace std;

const int ALPHABET_LENGTH = 26;
string alphabet = "abcdefghijklmnopqrstuvwxyz";
unordered_map<char, int> abc_map;

int main() {
    for (int i = 0; i < alphabet.size(); i++) {
        abc_map[alphabet[i]] = i;
    }

    int n, m;
    cin >> n >> m;
    cin.ignore();

    vector<vector<int>> mrr(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char c;
            cin >> c;
            mrr[i][j] = abc_map[c];
        }
    }

    vector<vector<int>> rows(n, vector<int>(ALPHABET_LENGTH, 0));
    vector<vector<int>> cols(m, vector<int>(ALPHABET_LENGTH, 0));

    set<int> rowset, colset;
    for (int i = 0; i < n; i++) rowset.insert(i);
    for (int j = 0; j < m; j++) colset.insert(j);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int x = mrr[i][j];
            rows[i][x]++;
            cols[j][x]++;
        }
    }

    auto check = [](vector<int>& counter) {
        int sum = 0, max = 0;
        for (int i : counter) {
            sum += i;
            if (i > max) max = i;
        }
        return sum == max && max >= 2;
    };

    bool flag = true;
    while (flag) {
        flag = false;
        set<int> rowset_to_remove, colset_to_remove;

        for (int i : rowset) {
            if (check(rows[i])) {
                flag = true;
                rowset_to_remove.insert(i);
            }
        }

        for (int j : colset) {
            if (check(cols[j])) {
                flag = true;
                colset_to_remove.insert(j);
            }
        }

        for (int i : rowset_to_remove) rowset.erase(i);
        for (int j : colset_to_remove) colset.erase(j);

        for (int i : rowset) {
            for (int j : colset_to_remove) {
                int x = mrr[i][j];
                rows[i][x]--;
            }
        }

        for (int j : colset) {
            for (int i : rowset_to_remove) {
                int x = mrr[i][j];
                cols[j][x]--;
            }
        }
    }

    cout << rowset.size() * colset.size() << endl;

    return 0;
}