#include <iostream>

using namespace std;

int main() {

	/*
	���淶Χ�ڵ�����1~10Ϊ��Ч����������10�����ݣ���������Ч����
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