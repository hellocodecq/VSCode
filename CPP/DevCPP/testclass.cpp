#include <iostream>

using namespace std;

int main() {
	int len = 100
	char map[len];
	for (int i = 0; i < len; i++)	// ³õÊ¼»¯
		map[i] = ' ';
	map[0] = '#';
	map[len-1] = '#';

	int p = 5;
	int head = 1;

	while (true) {
		map[p] = '*';
		for (int i = 0; i < len; i++)
			cout << map[i];
		cout << endl;
		map[p] = ' ';
		p += head;
		if (p >= len-2 or p <= 1) {
			head = -head;
		}
	}
}