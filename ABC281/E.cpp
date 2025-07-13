#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    vector<int> b = a;

    sort(b.begin(), b.begin()+m);
    multiset<int> l, r;
    ll ans = 0;
    for (int i = 0; i < m; i++){
        if (i < k) {
            l.insert(b[i]);
            ans += b[i];
        }
        else r.insert(b[i]);
    }
    cout << ans << " ";

    if (m == k) {
        for (int i = 0; i < n-m; i++){
            ans = ans-a[i]+a[i+m];
            cout << ans << " ";
        }
        cout << endl;
        return 0;
    }
    
    for (int i = 0; i < n-m; i++){
        if (a[i] < *r.begin()){
            l.erase(l.find(a[i]));
            ans -= a[i];
        }
        else r.erase(r.find(a[i]));

        if (a[i+m] <= *r.begin()) {
            l.insert(a[i+m]);
            ans += a[i+m];
        }
        else r.insert(a[i+m]);

        if (l.size() < k){
            int min = *r.begin();
            r.erase(r.find(min));
            l.insert(min);
            ans += min;
        }
        if (l.size() > k){
            int max = *l.rbegin();
            l.erase(l.find(max));
            r.insert(max);
            ans -= max;
        }

        cout << ans << " ";
    }
    cout << endl;
}