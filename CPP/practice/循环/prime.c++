#include <iostream>

using namespace std;

int main(){
    bool flag = true;   //是不是质数

    for(int a=2;a <101;a++){
        flag = true;
        for(int i=2;i<a;i++){
            if (a % i== 0) {
                flag = false;
                break;
            }
        }
        
        if(flag==true)
            cout << a <<endl;
}

}