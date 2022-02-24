#include <iostream>

using namespace std;

int main(){
    char map[10];
    for(int i=0;i<10;i++)
        map[i] = ' ';
    map[0] = '*';
    map[9] = '*';

    int p = 6;
    int a;
    int count;
    while (true){
        map[p] = '#';
        count = 0;
        for(int i=0;i<10;i++){
            cout << map[i];
            if (map[i]==' ')
                count ++;
        }
        if(count==0){
            cout << "游戏胜利 " <<endl;
            return 0;
        }
        cout << endl;
        
        cin >> p;
        if (map[p]!=' '){
            cout << "游戏失败！"<<endl;
            return 0;
        }
    }


    
}