#include <bits/stdc++.h>
#pragma GCC optimize("O3")
using namespace std;

// effective for hacking CPython's defaultdict
// To use run:
// g++ -std=c++17 -o tmp.out -Wall -Wno-unknown-pragmas $1.cpp
// Source: https://codeforces.com/contest/1625/hacks/781164/test
// Blog: https://codeforces.com/blog/entry/98994

mt19937 rng(123456789);

int randint(int a, int b){
    uniform_int_distribution<int> dist(a, b);
    return dist(rng);
}

int randint2(int a){
    return randint(0, a-1);
}

// parameter on how hard to try to find a long probing chain for the insertion of the Mth element
const int K = 14;

// do not change this
const int M = (2<<K)/3;

// size of resulting hack array, N must be at least M
const int N = 20000;

// heuristic on how hard to try to find the element that produces the longest probing chain
const int MAX_TRIES = 4000;

// maximum value in output hack array, minimum value is 1
const int MAX_SIZE = 150000;

bitset<(1<<K)+5> found;
int a[200005];

const int mask = (1<<K)-1; // must be 1 less than a power of 2

// This is how CPython probes the hash table.
/*
The 'score' here is the number of probes that are required before finding an empty element
to insert to.
*/
int findNextPythonHashIndx(int x, int &score){
    int indx = x&mask;
    score ++;
    if(!found[indx]){return indx;}
    int offset = x;
    while(1){
        offset >>= 5;
        indx = (indx*5 + 1 + offset)&mask;
        score ++;
        if(!found[indx]){return indx;}
    }
    return -1;
}

int findNextPythonHashIndx(int x){
    int score = 0;
    return findNextPythonHashIndx(x, score);
}

void insertPythonHash(int x){
    found[findNextPythonHashIndx(x)] = true;
}

bitset<MAX_SIZE+5> used;

int main(){
    // The total score is the estimated total number of hash collisions in the CPython hashing algorithm
    // It does not account for the resizing in CPython hash tables where there will be more insertions,
    // hence the estimate is likely conservative.
    long long totalScore = 0;

    int mostRecentBestScore = 0;
    for(int i = 0; i < M; i ++){
        // greedy algorithm: choose the element that causes the greatest number of hashing collisions
        int bestScore = 0;
        int bestVal = -1;
        int j = MAX_TRIES;
        while(j > 0){
            int x = randint(1, MAX_SIZE);
            if(used[x]){continue;}
            j --;

            int score = 0;
            findNextPythonHashIndx(x, score);
            if(score > bestScore){
                bestScore = score;
                bestVal = x;
            }
        }
        insertPythonHash(bestVal);
        used[bestVal] = true;

        a[i] = bestVal;
        mostRecentBestScore = bestScore;
        totalScore += bestScore;
    }

    for(int i = M; i < N; i ++){
        a[i] = a[M-1];
        totalScore += mostRecentBestScore;
    }

    /* Insert hack test code here. */
    int t = min(100, 300000/N);
    //printf("Total number of hash probes required: %lld\n", totalScore*t);
    //return 0;

    printf("%d\n", t);
    while(t --){
        printf("%d\n", N);
        for(int i = 0; i < N; i ++){
            printf("%d%c", a[i], (i == (N-1)) ? '\n' : ' ');
        }
    }
}