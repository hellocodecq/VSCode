#include <iostream>
using namespace std;

int main() {
	int n, m, total = 0;
	cin >> n;
	int list[n];
	for (int i = 0; i < n; i++)
		cin >> list[i];
	cin >> m;
	for (int i = 0; i < n; i++)
		if (list[i] != m)
			total += list[i];
	cout << total;
	return 0;
}
