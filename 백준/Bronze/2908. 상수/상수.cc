#include <iostream>
using namespace std;

int main() {
	int A;
	int B;
	cin >> A;
	cin >> B;

	int a_100 = A / 100;
	int a_10 = (A - 100 * a_100) / 10;
	int a_1 = A - (100 * a_100 + 10 * a_10);

	int b_100 = B / 100;
	int b_10 = (B - 100 * b_100) / 10;
	int b_1 = B - (100 * b_100 + 10 * b_10);
	

	int new_num1 = a_1 * 100 + a_10 * 10 + a_100;
	int new_num2 = b_1 * 100 + b_10 * 10 + b_100;

	if (new_num1 < new_num2)
	{
		cout << new_num2;
	}
	else
	{
		cout << new_num1;
	}
}