#include <iostream>

using namespace std;

int main(){

    string isbn;
    cin >> isbn;


    int total = 0;
    int j = 1;
    for(int i=0;i<isbn.size()-2;i++){
        if (isdigit(isbn[i])){
            total += (isbn[i]-'0') * j;
            cout <<  (isbn[i]-'0') << " " << j << endl;
            j++;
        }
    }

    total = total % 11;
    if (total == isbn[isbn.size()-1]-'0')
        cout << "right";
    else
        cout << total;
}