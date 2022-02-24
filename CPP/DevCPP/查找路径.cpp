#include <iostream>

using namespace std;

int main() {

	int m, n;	//

	cin >> m >> n;
	if (m < n) {
		int t = m;
		m = n;
		n = m;
	}
	int total = 0;	// 1~3
	for (int i = m; i > 0; i--) {	// 每行
		// 每一行的值：
		for (int j = n; j > 0; j--)
			total += j;

		n--;
	}
	cout << total;


	// 每行的情况：从1累加，加到
	/*

	*/



	return 0;
}