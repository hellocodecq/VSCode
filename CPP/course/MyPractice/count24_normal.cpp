#include<iostream>

using namespace std;

int main(){
    // int a, b, c, d;
    // cin >> a >> b >> c >> d;

    for (int a=0;a<5;a++)
        for(int b=0;b<5;b++)
            for(int c=0;c<5;c++)
                for( int d=0;d<5;d++)
        {
        cout << a << " " << b << " " << c << " " << d <<" : "; 
        int res = 0, x;
        x = a + b + c + d;
        if(x == 24) res ++;
        x = a + b + c - d;
        if(x == 24) res ++;
        x = a + b + c * d;
        if(x == 24) res ++;
        x = a + b - c + d;
        if(x == 24) res ++;
        x = a + b - c - d;
        if(x == 24) res ++;
        x = a + b - c * d;
        if(x == 24) res ++;
        x = a + b * c + d;
        if(x == 24) res ++;
        x = a + b * c - d;
        if(x == 24) res ++;
        x = a + b * c * d;
        if(x == 24) res ++;
        x = a - b + c + d;
        if(x == 24) res ++;
        x = a - b + c - d;
        if(x == 24) res ++;
        x = a - b + c * d;
        if(x == 24) res ++;
        x = a - b - c + d;
        if(x == 24) res ++;
        x = a - b - c - d;
        if(x == 24) res ++;
        x = a - b - c * d;
        if(x == 24) res ++;
        x = a - b * c + d;
        if(x == 24) res ++;
        x = a - b * c - d;
        if(x == 24) res ++;
        x = a - b * c * d;
        if(x == 24) res ++;
        x = a * b + c + d;
        if(x == 24) res ++;
        x = a * b + c - d;
        if(x == 24) res ++;
        x = a * b + c * d;
        if(x == 24) res ++;
        x = a * b - c + d;
        if(x == 24) res ++;
        x = a * b - c - d;
        if(x == 24) res ++;
        x = a * b - c * d;
        if(x == 24) res ++;
        x = a * b * c + d;
        if(x == 24) res ++;
        x = a * b * c - d;
        if(x == 24) res ++;
        x = a * b * c * d;
        if(x == 24) res ++;
        cout << res << endl;
} 
    return 0;
}