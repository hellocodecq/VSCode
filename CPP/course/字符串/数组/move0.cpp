#include <iostream>

using namespace std;

int main(){
    // 给定一个数组，将所有的0移动到后面
    // 例如[1,0,2,0,3,0]  -> [1,2,3,0,0,0]
    int n;
    cin >>n;
    int list1[n], list2[n];
    for(int i=0;i<n;i++){
        cin >> list1[i];
    }

    int index=0;
    for(int i=0;i<n;i++){
        if (list1[i]!=0){
            list2[index] = list1[i];
            index++;
        }
    }
    for(;index<n;index++)
        list2[index] = 0;
    for(int i=0;i<n;i++)
        cout << list2[i] << " ";

    return 0;
}