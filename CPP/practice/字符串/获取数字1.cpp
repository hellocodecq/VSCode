#include <iostream>

using namespace std;

int main(){

    string a;
    cin >> a;
    a += ' ';

    string b="";
    for (int i=0;i<a.size();i++){
        if (isdigit(a[i])){
            b += a[i];
        }
        else{
            if (b!=""){
                cout << b << " ";
                b = "";
            }
        }

    }

    return 0;
}