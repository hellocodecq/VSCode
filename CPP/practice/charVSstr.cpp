#include <iostream>

using namespace std;

/*
	头文件代码查错，完成到 '<'
*/

int main() {
	
	string a;
	getline(cin, a);
	a += " ";
	int i;
	for(i=0;i<a.size();i++){		// 判断 #
		if(a[i]!=' '){
			if (a[i]=='#'){
				cout << "# 没问题" << endl;
				break;
			}
			else{
				cout << "# 错误！" << endl;
				return 0;
			}
		}
	}
	string include = "";
	for( i++; i<a.size();i++ ){
		if(a[i]!=' '){
			for( ; a[i]!=' ' and a[i]!='<';i++ ){
				include += a[i];
			}
			break;
		}
	}
	if(include == "include")
		cout << "include 没问题" << endl;
	else{
		cout << "include 错误！" << include << ".";
		return 0;
	}

	for(;i<a.size();i++){	// 判断尖括号
		if(a[i]!=' '){
			if (a[i]=='<'){
				cout << "< 没问题" << endl;
				break;
			}else{
				cout << "< 错误！";
				return 0;
			}
		}
	}


}