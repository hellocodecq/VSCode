#include <iostream>

using namespace std;

int MyAtoI(string str){

    int size = str.size(), num=0;
    int i=0;
    for(i=0;str[i]==' ' && i<size;i++);    // 判断到第一个非空格
    if (i==size)
        return 0;

    bool flag = false;  // 判断负数

    if (str[i]=='-')        // 判断第一个非空字符
        flag = true;
    else if(str[i]=='+');
    else if(isdigit(str[i])){
        num = str[i]-'0';
    }
    else
        return 0;

    for(i++;i<size;i++){
        if (isdigit(str[i]))
            num = num*10 +(str[i]-'0');
        else
            break;
    }
    if (flag)
        return -num;

    return num;
}


int main(){

    string a;
    getline(cin , a);
    int num = MyAtoI(a);
    cout << num;

    return 0;
}