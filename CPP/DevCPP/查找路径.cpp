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
	for (int i = m; i > 0; i--) {	// ÿ��
		// ÿһ�е�ֵ��
		for (int j = n; j > 0; j--)
			total += j;

		n--;
	}
	cout << total;


	// ÿ�е��������1�ۼӣ��ӵ�
	/*

	*/



	return 0;
}