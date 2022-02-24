#include <iostream>

using namespace std;

int main() {

	char map[10];
	for (int i = 0; i < 10; i++)
		map[i] = ' ';
	map[0] = '*';
	map[9] = '*';

	int p = 5;
	int spd = 1;
	string a;

	while (true) {
		map[p] = '#';
		for (int i = 0; i < 10; i++)
			cout << map[i];
		cout << endl;
		map[p] = ' ';

		p += spd;

		if (p == 1 or p == 8)
			spd = -spd;

	}
	return 0;
}