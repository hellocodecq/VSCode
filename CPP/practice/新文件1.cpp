#include <iostream>
using namespace std;

int main() {

    
string c_num[10] = {"零","一","二","三","四","五","六","七","八","九"};
int a;
cin >> a;
int g = a % 10;
int s = a / 10 % 10;
int b = a / 100;
cout << c_num[b] << "百";

if (s>0){
    cout << c_num[s] << "十";
    if (g>0)
        cout << c_num[g];
}
else{
    if(g>0)
        cout <<"零" << c_num[g];
}
}