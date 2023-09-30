#include <vector>
#include <algorithm>

struct Tuple {
    int left_val;
    int left_cnt;
    int right_val;
    int right_cnt;
    int max_zero;
    int max_one;
    int cur_len;
};

void solve(int n, int q, std::string srr, std::vector<std::vector<int>> qrr) {

    std::vector<Tuple> arr;
    for (char x : srr) {
        if (x == '1') arr.push_back({1, 1, 1, 1, 0, 1, 1});
        else arr.push_back({0, 1, 0, 1, 1, 0, 1});
    }

    // op function
    auto op = [](Tuple x, Tuple y) -> Tuple {
        int cur_len_all = x.cur_len + y.cur_len;

        if (x.cur_len == 0) return y;

        if (y.cur_len == 0) return x;

        int max_zero_all = std::max(x.max_zero, y.max_zero);
        int max_one_all = std::max(x.max_one, y.max_one);

        if (x.right_val == y.left_val && x.right_val == 0) {
            max_zero_all = std::max(max_zero_all, x.right_cnt + y.left_cnt);
        }

        if (x.right_val == y.left_val && x.right_val == 1) {
            max_one_all = std::max(max_one_all, x.right_cnt + y.left_cnt);
        }

        if (x.max_zero == x.cur_len && y.left_val == 0) {
            x.left_cnt += y.left_cnt;
        }

        if (x.max_one == x.cur_len && y.left_val == 1) {
            x.left_cnt += y.left_cnt;
        }

        if (y.max_zero == y.cur_len && x.right_val == 0) {
            y.right_cnt += x.right_cnt;
        }

        if (y.max_one == y.cur_len && x.right_val == 1) {
            y.right_cnt += x.right_cnt;
        }

        return {x.left_val, x.left_cnt, y.right_val, y.right_cnt, max_zero_all, max_one_all, cur_len_all};
    };

    Tuple e = {0, 0, 0, 0, 0, 0, 0};

    // mapping function
    auto mapping = [](int x, Tuple y) -> Tuple {
        if (!x) return y;
        return {1 - y.left_val, y.left_cnt, 1 - y.right_val, y.right_cnt, y.max_one, y.max_zero, y.cur_len};
    };

    int id_ = 0;
    int f = 1;

    // Initialize LazySegTree 'st' here with 'op', 'e' and 'mapping' functions.

    for (auto v : qrr) {
        int c = v[0], l = v[1], r = v[2];
        if (c == 2) {
            std::cout << st.prod(l - 1, r).max_zero << std::endl;
        } else {
            st.apply(l - 1, r, f);
        }
    }
}