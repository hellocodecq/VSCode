# include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int a[11];

	string num_cn[10] = {"��", "һ", "��", "��", "��", "��", "��", "��", "��", "��"};
	int index;
	for (index = 0; n != 0; index++) {
		a[index] = n % 10;
		n /= 10;
	}

	for ( index--; index >= 0; index--  ) {
		cout << num_cn[ a[index]  ];
	}
}