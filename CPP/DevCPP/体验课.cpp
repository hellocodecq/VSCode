#include <iostream>

// ʹ�� ���ֿռ� std
using namespace std;

int main() {

	cout << "��ӭѧϰC++" << endl ;
	cout << "���Ǳ�̻����ˣ����кܶ๦��" << endl;
	cout << "1. ���ӷ��� 2. ��ʾͼƬ��3. ����ʫ" << endl;
	int a;	
	cin >> a;
	cout << "�������ˣ�" << a << endl;


	if (  a == 1  ) {
		cout << "���ӷ�" << endl;
		int b,c;
		cout << "�������������֣�";
		cin >> b >> c;
		int d = b+c;
		cout << "���������ֵĺ��ǣ�" << d << endl;
		
	} else if ( a == 2  ) {
		system(	"pic.png"	);

	} else if (a == 3) {
		cout << "�����յ���, ���κ�������˭֪���в�, ���������ࡣ";
	}



}