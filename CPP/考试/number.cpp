#include<iostream>

using namespace std;

int main(){

    int n, g, s, b;
    cin >> n;
    int count = 0;
    int max = n*100+(n-1)*10+n-2;
    for(int i=102;i<=max;i++){
        g = i % 10;
        s = i / 10 % 10;
        b = i / 100;
        if (g <= n and s <= n and b <= n)
            if (b!=s and b!=g and s!=g){
                if (g%2==1){
                    count ++;
                }
            }
    }
    cout << count ;
}