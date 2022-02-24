# include <iostream>	// 导入 基本输出输出库

using namespace std;

int main() {		// 主函数，程序从这运行
	int a;
	int sum = -1;		// 保存最大值
	int low = 101;		// 保存最小值
	for (int i = 0; i < 5; i++) {
		cin >> a;
		if (a > sum) {
			sum = a;
		} 
		if (a < low) {
			low = a;
		}

	}
	cout << sum - low;

	return 100;
}