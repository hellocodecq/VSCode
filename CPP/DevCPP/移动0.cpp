#include <iostream>

using namespace std;

int main() {
	int my = 8;
	for (int i = 0; i < 10; i++) {
		cout << my - 1 << endl;
		my += my - 1;
	}


//	int n = 10;
//	int enemy [10];
//	int my = 5;
//	for (int i = 0; i < 10; i++)
//		cin >> enemy[i];
//
//	int count = 0;
//	int i = 0;
//	while (true) {
//		for (i = 0; i < 10; i++) {
//			if (my > enemy[i] and enemy[i] != 0) {
//				my += enemy[i];
//				enemy[i] = 0;
//				count ++;
//				break;
//			}
//		}
//		if (count >= 10) {
//			cout << "ÓÎÏ·Ê¤Àû " << my << endl;
//			return 0;
//		}
//		if (i >= 10) {
//			cout << "ÓÎÏ·Ê§°Ü " << count << endl;
//			return 0;
//		}
//
//	}


	return 0;
}