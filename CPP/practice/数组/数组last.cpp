#include <iostream>
#include <ctime>

using namespace std;

int main(){

    int player1[26], player2[26], cards[14];
    int index1 = 0, index2 = 0;

    for(int i=0;i<14;i++)
        cards[i] = 0;

    srand((int)time(NULL));
    // 玩家1
    while(index1<26){
        int card = rand()%13+1;
        if (cards[card]>=4)
            continue;
        cards[card]++;
        player1[index1] = card;
        index1++;
    }
    for(int i=0;i<index1;i++)
        cout << player1[i] <<" ";

    cout << endl;
    // 玩家2
    while(index2<26){
        
        int card = rand()%13+1;
        if (cards[card]>=4)
            continue;
        cards[card]++;
        player2[index2] = card;
        index2++;
    }
    for(int i=0;i<index2;i++)
        cout << player2[i] <<" ";

    cout << endl;

    for(int i=0;i<26;i++){
        // player1[i] => 当前拿到的牌
        for(int j=i+1;j<26;j++){
            if (player1[i]==player1[j]){
                player1[i] = 0;
                player1[j] = 0;
                break;
            }
        }
    }
    for(int i=0;i<26;i++)
        if(player1[i]!=0)
            cout << player1[i] << " ";



















    // int n, a, index = 0;
    // cin >> n;
    // int list[n], j;
    // for(int i=0;i<n;i++){       
    //     cin >> a;           // 输入数据
    //     for(j=0;j<index;j++){       // 遍历已有的数字列表
    //         if (a == list[j])       // 如果出现过
    //             break;              // 直接退出循环
    //     }
    //     if (j==index){              // 循环结束后，判断循环次数
    //         list[index] = a;        // 如果循环次数和列表长度相等，说明遍历完没有重复，添加数据
    //         index++;                // 下标+1，因为添加了数据
    //         cout << a <<' ';        // 输出这个数据，因为它没有重复
    //     }
    // }

    

    // int list[10], ou[10],ji[10];

    // for(int i=0;i<10;i++)
    //     cin>> list[i]

    // int index_ji = 0, index_ou = 0;
    // for(int i=0;i<10;i++){
    //     if (list[i]%2 == 0){
    //         ou[index_ou] = list[i];
    //         index_ou ++;
    //     }
    //     else{
    //         ji[index_ji] = list[i];
    //         index_ji ++;
    //     }
    // }


    // -----------------------------------
    // int a[10];
    // for(int i=0;i<10;i++)
    //     cin>> a[i];    
    // for(int i=0;i<10;i++){
    //     if (a[i] > 10 or a[i] < 1)
    //         a[i] = 0;

    // for(int i=0;i<10;i++)
    //     if (a[i]!=0)
    //         cout << a[i] << ' ';
}