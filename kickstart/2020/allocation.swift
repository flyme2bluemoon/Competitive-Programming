// let T = Int(readLine()!)!

// func getLine() -> [Int] {
//     let stringArray = readLine()!.split(separator: " ")
//     let lengthOfInput = stringArray.count
//     var intArray: [Int] = []
//     for i in 0..<lengthOfInput {
//         intArray.append(Int(stringArray[i]) ?? 0)
//     }
//     return intArray
// }

// for i in 1...T {
//     var house = 0
//     var n = getLine()
//     var b = getLine()

//     b.sort()

//     for j in 0..<n[0] {
//         n[1] -= b[j]
//         if n[1] >= 0 {
//             house += 1
//         }
//     }

//     print("Case #" + String(i) + ": " + String(house))
// }


#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ar array

int n, b, a[100000];

void solve() {
	c in >> n >> b;
	for(int i=0; i<n; ++i)
		cin >> a[i];
	sort(a, a+n);
	int ans=0;
	for(int i=0; i<n; ++i) {
		if(b>=a[i]) {
			b-=a[i];
			++ans;
		}
	}
	cout << ans << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t, i=1;
	cin >> t;
	while(t--) {
		cout << "Case #" << i << ": ";
		solve();
		++i;
	}
}