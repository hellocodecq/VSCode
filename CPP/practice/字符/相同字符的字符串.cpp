#include <iostream>

using namespace std;

int main(){


    string a, b;
cin >> a >> b;
int count = 0;
if(a.size()!=b.size()){
    cout << "NO";
    return 0;
}
for (int i = 0; i < a.size(); i++) {
    for (int j = 0; j < b.size(); j++) {
        if (a[i] == b[j]) {
            count++;
            cout << a[i] << ":" << b[i] << "\t";
            cout << a << " " << b << endl;
            a[i] = ' ';
            b[j] = ' ';
            break;
        }
    }
}
cout << count << " " << a.size() << a << b << endl;
if (count == a.size())
    cout << "相同";
else
    cout << "不同";
}