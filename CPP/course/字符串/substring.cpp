#include <iostream>

using namespace std;

int main(){

    string a, b="";
    getline(cin, a);
    int size = a.size();
    for(int i=0;i<size;i++){
        if(isalnum(a[i]))
            b+=tolower(a[i]);
    }
    cout << "字符串b：" << b << endl;
    size = b.size();
    bool flag = true;
    for(int i=0;i<size/2;i++){
        if(b[i]!=b[size-i-1]){
            cout << "第" <<i << "个: " << b[i] << " : " << b[size-i-1] <<endl;
            flag=false;
            break;
        }
    }
    if (flag)
        cout << "True";
    else   
        cout << "False";




    return 0;
}