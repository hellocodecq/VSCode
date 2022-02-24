//#include <iostream>
//
//using std::cout;

void swap(int *a, int *b) {

	int c;
	c = *a;
	*a = *b;
	*b = c;

}

int main() {
	int a = 6;
	int b = 1;
	swap(&a, &b);


	return int(a - b);

}