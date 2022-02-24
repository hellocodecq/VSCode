#include <iostream>

using namespace std;

int main(){
    string isbn;
cin >> isbn;
int num[10];
int index = 0;
for (int i = 0; i < isbn.size(); i++) {
    if (isbn[i] != '-') {
        num[index] = isbn[i] - 48;
    	index++;
	}
}	
int total = 0;
for (int i = 0; i < index - 1; i++)
total += (i + 1) * num[i];
total = total % 11;
if (total == 10)
	total = 'X';
if (total == num[index - 1])
	cout << "Right";
else {
    for (int i = 0; i < isbn.size() - 1; i++)
        cout << isbn[i];
    if (total > '9')
        cout << 'X';
    else
        cout << total;
}
}