#include <iostream>

using namespace std;

/*
    1. 字符的定义与简单使用
    2. 字符与数字的强制转换
    3. 数字与字符的强制转换
    4. is函数：isalpha isdigit isupper islower isalnum(数字或字母) isspace tolower toupper

*/

int main(){
// 演示: 字符转数字
    // char a;
    // cout << "请输入一个字符：";
    // cin >> a;
    // cout << "你输入了：" << a << "\n它的编号："<<int(a) << endl;
// 小练习-数字转字符
    // int b;
    // cout << "请输入一个数字:" ;
    // cin >> b;
    // cout << "你输入了：" << b << "\n它的字符："<<char(b) << endl; 

// 演示： 字符的加法
    // char a = 'a';
    // cout <<"输入：" << a << endl;
    // char b = a + 2;
    // cout << "+2= " << b << endl;
// 练习-字符的四则运算
    // char c = a - 2;
    // cout << "-2= " << c << endl;
    // char d = a*2;
    // cout << "*2= " << d << endl;
    // char e = a/2;
    // cout << "-2= " << e << endl;

    // if(isdigit(a)){
    //     cout << a << "是一个数字" << endl;
    // }
    // else{
    //     cout << a << "不是一个字母" << endl;
    // }
    // if (isalpha(b))
    //     cout << b << "是一个字母" << endl;
    // else
    //     cout << b << "不是一个字符" << endl;

// 演示：遍历字符串，取出字符
// string a = "ABC";
// string b = "";
// for (int i=0;i<a.size();i++){
//     b += tolower(a[i]);
// }
// cout << b;
    
// 练习
string a, b="";
cin >> a;
for(int i=0;i<a.size();i++){
    if(isalpha(a[i])){
        if (islower(a[i]))
            b += toupper(a[i]);
    	else
            b += tolower(a[i]);
    }
}
cout << b;

}