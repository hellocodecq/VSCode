#include <iostream>

using namespace std;

int main() {

	/*
	保存范围内的数：1~10为有效整数，输入10个数据，保存其有效数据
	*/
	int list[10];
	int index = 0;
	int a;
	for (int i = 0; i < 10; i++) {
		cin >> a;
		if (a >= 1 and a <= 10) {
			list[index] = a;
			index++;
		}
	}
	for (int i = 0; i < index; i++)
		cout << list[i] << " ";


}