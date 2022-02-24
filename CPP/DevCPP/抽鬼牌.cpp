#include <iostream>
#include <ctime>

using namespace std;

int main() {

	int player1[26], player2[26];

	srand((int)time(NULL));
	
	int cards[13];
	for(int i=0;i<13;i++)
		cards[i] = 0;
	
	int card;
	for(int i=0;i<26;i++){
		while(true){
			card = rand()%13 + 1;
			if (cards[card]<4)
				break;
		}
		cards[card]++;
		player1[i] = card;
	}
	for(int i=0;i<26;i++)
		cout << player1[i] << " ";
	cout << endl;
	//----------------


	return 0;
}