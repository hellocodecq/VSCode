#include <iostream>
using namespace std;

int Add(int a,int b)
{
        return a + b;
}
int Subtract(int a,int b)
{
        return a - b;
}
int Multiply(int a,int b)
{
        return a * b;
}
int (*Handles[3])(int, int) = { Add,Subtract,Multiply };
int Nums[4];
int (*Func[3])(int, int);
int offsetNum = 0, offsetFunc = 0;

int main()
{
        
        int a, b, c, d,res = 0;
        cin >> a >> b >> c >> d;
        for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                        for (int k = 0; k < 3; k++) {
                                offsetNum = 0;
                                offsetFunc = 0;
                                Nums[offsetNum++] = a;
                                if (i < 2) {
                                        Func[offsetFunc++] = Handles[i];
                                        Nums[offsetNum++] = b;
                                }
                                else 
                                        Nums[offsetNum - 1] = Handles[i](Nums[offsetNum - 1], b);
                                if (j < 2) {
                                        Func[offsetFunc++] = Handles[j];
                                        Nums[offsetNum++] = c;
                                } else
                                        Nums[offsetNum - 1] = Handles[j](Nums[offsetNum - 1], c);
                                if (k< 2) {
                                        Func[offsetFunc++] = Handles[k];
                                        Nums[offsetNum++] = d;
                                } else
                                        Nums[offsetNum - 1] = Handles[k](Nums[offsetNum - 1], d);
                                while (offsetFunc > 0) {
                                        Nums[offsetNum - 2] = Func[--offsetFunc](Nums[offsetNum - 2], Nums[offsetNum - 1]);
                                        offsetNum--;
                                }
                                if (Nums[0] == 24)
                                        res++;
                        }
                }
        }
        cout << res;
        return 0;
}