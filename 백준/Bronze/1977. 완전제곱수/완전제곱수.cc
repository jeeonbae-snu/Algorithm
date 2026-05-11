#include <iostream>
using namespace std;

int main() {
	int M, N;
	cin >> M;
	cin >> N;
	int sum = 0;
	int num = 0;
	int arr[100];

	for (int i = 1; i <= 100; i++)//M=60 N=80 j=64가 나와야함
	{
		if (i*i >= M && i*i <= N) {
			sum += i*i ;
			arr[num] = i*i ;
			num++;
		}
	}
	if (sum == 0) {
		cout << -1;
		return 0;
	}
	else {
		cout << sum << endl;
		cout << arr[0];
	}
	
}