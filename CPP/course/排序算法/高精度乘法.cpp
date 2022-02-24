#include <iostream>

using namespace std;

int main() {

	string a, b;
	cin >> a >> b;
	cout << a.size() << " " << b.size() << endl;
	int int_a[a.size()];
	int int_b[b.size()];
	int max = a.size() > b.size() ? a.size() : b.size();

	memset(int_a, 0, a.size()*sizeof(int));
	memset(int_b, 0, b.size()*sizeof(int));

	for (int i = 0; i < a.size(); i++)
		int_a[i] = a[i] - '0';
	cout << endl;
	for (int i = 0; i < b.size(); i++)
		int_b[i] = b[i] - '0';


	int c[a.size() + b.size()];
	memset(c, 0, (a.size() + b.size())*sizeof(int));



}