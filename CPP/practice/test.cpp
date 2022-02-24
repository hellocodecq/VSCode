#include <iostream>

using namespace std;

int main() {

	string a;
	cin >> a;
	a += ' ';
	string list[a.size()];
	string tmp = "";
	int index = 0;
	for (int i = 0; i < a.size(); i++) {
		if (isdigit(a[i]))
			tmp += a[i];
		else if (tmp != "") {
			list[index] = tmp;
			index++;
			tmp = "";
		}
	}
	for (int i = 0; i < index; i++)
		cout << list[i].data() << " ";
	int total = 0;
	for (int i = 0; i < index; i++)
		total += stoi(list[i]);
	cout << endl << total;

}