#define SPEED \
    std::ios::sync_with_stdio(false); \
    cin.tie(NULL); \
    cout.tie(0);

#include <iostream>

using namespace std;

int main() {
    SPEED;

    int n;
    int r;
    cin >> n >> r;
    
    int powers[r];
    int t;
    
    for(int i = 0; i < r; i++) {
        cin >> t >> powers[i];        
    }

    int fib[50];
    fib[0] = 0;
    fib[1] = 1;

    for(int i = 2; i <= n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    int a_p;
    int b_p;
    
    if (n == 1){
        a_p = 1;
        b_p = 0;
    } else if (n == 2) {
        a_p = 0;
        b_p = 1;
    } else {
        a_p = fib[n - 2];
        b_p = fib[n - 1];
    }

    for(int i = 0; i < r; i++) {
        if ((a_p != 0 && powers[i] % a_p != 0) && (b_p != 0 && powers[i] % b_p != 0)) {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
    return 0;

}