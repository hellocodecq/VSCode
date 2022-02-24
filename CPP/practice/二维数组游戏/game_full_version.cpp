#include <iostream>

using namespace std;

int main(){
    int size = 10;
    char map[size][size];
    for (int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            map[i][j] = ' ';
        }
    }

    for(int i=0;i<10;i++){
        map[0][i] = '*';
        map[9][i] = '*';
        map[i][0] = '*';
        map[i][9] = '*';
    }

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            map[i][j] = '*';
            map[9-i][j] = '*';
            map[i][9-j] = '*';
            map[9-i][9-j] = '*';
        }
    }

    int x=5, y=5;

    while(true){
        system("cls");
        int count = 0;
        map[x][y] = '#';
        for (int i=0;i<size;i++){
            for(int j=0;j<size;j++){
                cout << map[i][j];
                if(map[i][j]!=' ')      // 遍历每个格子，不是空的，计数器+1
                    count++;
            }
            cout << endl;
        }
        if(count==size*size){   // 判断计数器，如果非空格子的数量与地图大小一致
            cout << "胜利";     // 表明整个地图已经填充完了，则游戏胜利
            system("pause");
            return 0;
        }
        // 否则就说明没有填充完，则判断 # 的上下左右有没有空的，如果没有，就说明没路走了，游戏失败
        else if(map[x-1][y]!=' ' and map[x+1][y]!=' ' and map[x][y-1]!=' ' and map[x][y+1]!= ' '){
            cout << "失败！";
            system("pause");
            return 0;
        }
        char cmd;  
        cin >> cmd;
        // map[x][y] = ' ';    //不把它注释掉，原来的 # 就会变成空字符，
                              // 注释掉，就还是 # ，通过这种方式来切换是否要留 # 在原地
        if (cmd =='w'){
            x --;
            if (map[x][y] !=' ')    // 判断能不能走，只需要判断空字符就可以了，空字符能走，其它不能
                x ++;
        }
        else if(cmd=='s'){
            x++;
            if (map[x][y] !=' ')
                x --;
        }
        else if (cmd=='d'){
            y++;
            if (map[x][y] !=' ')
                y --;
        }
        else if (cmd=='a'){
            y--;
            if (map[x][y] !=' ')
                y ++;
        } 
    }
}