#include <iostream>

// 使用 名字空间 std
using namespace std;

int main() {

	cout << "欢迎学习C++" << endl ;
	cout << "我是编程机器人，我有很多功能" << endl;
	cout << "1. 做加法， 2. 显示图片，3. 背古诗" << endl;
	int a;	
	cin >> a;
	cout << "你输入了：" << a << endl;


	if (  a == 1  ) {
		cout << "做加法" << endl;
		int b,c;
		cout << "请输入两个数字：";
		cin >> b >> c;
		int d = b+c;
		cout << "这两个数字的和是：" << d << endl;
		
	} else if ( a == 2  ) {
		system(	"pic.png"	);

	} else if (a == 3) {
		cout << "锄禾日当午, 汗滴禾下土。谁知盘中餐, 粒粒皆辛苦。";
	}



}