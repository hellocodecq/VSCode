# include <iostream>	// ���� ������������

using namespace std;

int main() {		// �������������������
	int a;
	int sum = -1;		// �������ֵ
	int low = 101;		// ������Сֵ
	for (int i = 0; i < 5; i++) {
		cin >> a;
		if (a > sum) {
			sum = a;
		} 
		if (a < low) {
			low = a;
		}

	}
	cout << sum - low;

	return 100;
}