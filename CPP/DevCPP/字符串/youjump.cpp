#include <iostream>

using namespace std;

int main(){
    string msg,word;
getline(cin, msg);
for (int i = 0; i < msg.size(); i++) {
    if (msg[i] != ' ' and msg[i] != ',')
        word += msg[i];
    else {
        cout << word << endl;
        word = "";
    }
}
cout << word << endl;
}