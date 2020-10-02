#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int N, K, v[103];
	cin>>N>>K;

	for (int i = 0; i < N; ++i)	{
		cin>>v[i];
	}

	sort(v,v + N);

	int sum = 0;
	for (int i = 0; i < K; ++i)	{
		sum += v[i];
	}

	if(sum % 100 == 0)
		cout<<sum/100;
	else
		cout<<sum/100 + 1;

	system("pause");
	return 0;
}
