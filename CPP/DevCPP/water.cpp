#include <iostream>

using namespace std;

int main() {


	int n, m;

	cin >> n >> m;
	int list[n];



	for (int i = 0; i < n; i++)
		cin >> list[i];
	int index = m;
	int time = 0;

	while (true) {
		time++;

		for (int i = 0; i < m; i++) {
			list[i] -= 1;
			cout << list[i] << " ";
			if (list[i] <= 0) {
				if (index != n) {
					list[i] = list[index];
					list[index] = 0;
					index += 1;
				}
			}
		}
		cout << endl;
		cout << "ÁÐ±í£º";
		for (int i = 0; i < n; i++) {
			cout << list[i] << " ";
		}
		cout << endl;

		int j = 0;
		for (j = 0; j < n; j++) {
			if (list[j] > 0)
				break;
		}
		if (j == n)
			break;
//		cin >> j;
	}
	cout << time;


}