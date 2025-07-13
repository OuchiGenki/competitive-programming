#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define INF 100000000

int main() {
    int n;
    int a, b, c;
    cin >> n >> a >> b >> c;

    ll sum = 0;
    ll ans = INF;
    for(int i = 0; i < 10000; i++){
        for(int j = 0; j < 10000; j++){
            sum = a*i + b*j;
            if((n-sum) >= 0 && (n-sum)%c == 0){
                ans = min(ans, i+j+(n-sum)/c);
            }
        }
    }

    cout << ans << endl;
}