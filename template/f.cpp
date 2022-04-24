// from editorial, want to see how it looks like

#include <bits/stdc++.h>
 
using namespace std;
const int c=505;
int t, n, m, fix[c][c], ans[c][c], rotcnt, change, old_cl, new_cl;
int fix2[c][c], ans2[c][c];
void color_boundary() {
    for (int cnt=1; cnt<=2; cnt++) {
        for (int j=2; j<=m; j++) {
            if (!ans[1][j]) ans[1][j]=ans[1][j-1];
            if (ans[1][j]!=ans[1][j-1]) change++;
        }
        for (int i=2; i<=n; i++) {
            if (!ans[i][m]) ans[i][m]=ans[i-1][m];
            if (ans[i][m]!=ans[i-1][m]) change++;
        }
        for (int j=m-1; j>=1; j--) {
            if (!ans[n][j]) ans[n][j]=ans[n][j+1];
            if (ans[n][j]!=ans[n][j+1]) change++;
        }
        for (int i=n-1; i>=1; i--) {
            if (!ans[i][1]) ans[i][1]=ans[i+1][1];
            if (ans[i][1]!=ans[i+1][1]) change++;
        }
        if (!ans[1][1]) ans[1][1]=1;
        if (cnt==1) change=0;
    }
}
void rotate_90() {
    rotcnt++;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            ans2[i][j]=ans[i][j], fix2[i][j]=fix[i][j];
        }
    }
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=m; j++) {
            ans[j][n+1-i]=ans2[i][j];
            fix[j][n+1-i]=fix2[i][j];
        }
    }
    swap(n, m);
}
void good_rotation() {
    for (int cnt=1; cnt<=4; cnt++) {
        bool same=1, opposite=0;
        for (int i=1; i<=n; i++) {
            if (ans[i][1]!=ans[1][1]) same=0;
            if (1<i && i<n && ans[1][1]!=ans[i][m]) opposite=1;
        }
        if (!same || !opposite) rotate_90();
    }
}
void color_the_stripes() {
    for (int i=2; i<n; i++) {
        for (int j=2; j<m; j++) {
            if (!fix[i][j]) {
                if (i%4==2 || i%4==3) ans[i][j]=old_cl;
                else ans[i][j]=new_cl;
            }
        }
    }
}
void avoid_touching() {
    for (int i=1; i<n; i++) {
        if (ans[i][m-1]==ans[i+1][m] && ans[i+1][m-1]==ans[i][m] && ans[i][m]!=ans[i+1][m]) {
            if (!fix[i][m]) ans[i][m]=3-ans[i][m];
            else ans[i+1][m]=3-ans[i+1][m];
        }
    }
}
void boundary_stripe_connection() {
    int first=0, last=0;
    for (int i=1; i<=n; i++) {
        if (ans[i][m]==new_cl) {
            if (!first) first=i;
            last=i;
        }
    }
    if (first==0 || (last>3 && first<n-2)) return;
    if (last<=3 && fix[4][m-1]==old_cl) {
        for (int i=3; i<=5; i++) {
            ans[i][m]=new_cl;
        }
        return;
    }
    if (first>=n-2 && fix[n-3][m-1]==old_cl) {
        for (int i=n-4; i<=n-2; i++) {
            ans[i][m]=new_cl;
        }
        return;
    }
    int x=(last<=3 ? 2 : n-2);
    for (int i=x; i<=x+1; i++) {
        for (int j=m-1; j<=m; j++) {
            if (!fix[i][j]) ans[i][j]=new_cl;
        }
    }
}
void connect_isolated_point(int x, int y) {
    if (ans[x-1][y]==new_cl || ans[x+1][y]==new_cl || ans[x][y+1]==new_cl) return;
    int x1=(x==2 ? 1 : n), x2=(x==2 ? 2 : n-1), x3=(x==2 ? 3 : n-2), x4=(x==2 ? 4 : n-3);
    if (y<=m-2 && ans[x1][y+2]==new_cl) {
        ans[x1][y]=new_cl;
        ans[x1][y+1]=new_cl;
        return;
    }
    if (y<=m-2 && ans[x2][y+2]==new_cl) {
        ans[x2][y+1]=new_cl;
        return;
    }
    if (fix[x4][y]!=old_cl) {
        ans[x3][y]=new_cl;
    } else {
        int y2=(y+1<m ? y+1 : y-1);
        ans[x2][y2]=new_cl;
        ans[x3][y2]=new_cl;
    }
}
void bridge_through_the_stripe(int x) {
    for (int j=2; j<=4; j++) {
        bool good=1;
        for (int i=x-1; i<=x+2; i++) {
            if (fix[i][j]==old_cl) good=0;
        }
        if (good) {
            ans[x][j]=new_cl;
            ans[x+1][j]=new_cl;
            return;
        }
    }
    for (int i=x-1; i<=x+2; i++) {
        if (!fix[i][3]) ans[i][3]=new_cl;
    }
    if (fix[x-1][3]) {
        ans[x-1][2]=old_cl;
        ans[x][4]=new_cl;
    }
    if (fix[x+2][3]) {
        ans[x+2][2]=old_cl;
        ans[x+1][4]=new_cl;
    }
    if (fix[x][3] || fix[x+1][3]) {
        ans[x][2]=new_cl;
        ans[x+1][2]=new_cl;
    }
}
int main()
{
    cin >> t;
    for (int tc=1; tc<=t; tc++) {
        cin >> n >> m;
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                char c;
                cin >> c;
                fix[i][j]=(c=='B' ? 1 : c=='W' ? 2 : 0);
                ans[i][j]=fix[i][j];
            }
        }
        color_boundary();
        if (change>=4) {
            cout << "NO\n";
        } else {
            good_rotation();
            old_cl=ans[1][1], new_cl=3-ans[1][1];
            color_the_stripes();
            avoid_touching();
            boundary_stripe_connection();
            for (int j=2; j<m; j++) {
                if (fix[2][j]==new_cl) connect_isolated_point(2, j);
                if (fix[n-1][j]==new_cl) connect_isolated_point(n-1, j);
            }
            for (int i=6; i<=n-6; i+=4) {
                if (ans[1][1]==ans[i][m] || ans[1][1]==ans[i+1][m]) bridge_through_the_stripe(i);
            }
            while (rotcnt<4) rotate_90();
            cout << "YES\n";
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=m; j++) {
                    cout << (ans[i][j]==1 ? "B" : "W");
                }
                cout << "\n";
            }
        }
        rotcnt=0, change=0;
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                fix[i][j]=0, ans[i][j]=0;
                fix[j][i]=0, ans[j][i]=0;
            }
        }
    }
    return 0;
}