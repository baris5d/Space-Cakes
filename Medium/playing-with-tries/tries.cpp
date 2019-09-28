#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define ull unsigned long long

ull pow2(int a, int b) {
    if (b==0) return 1;
    if (b==1) return a;
    ull r = pow2(a, b/2);
    return r*r*pow2(a,b%2);
}   

int find(int a, int l, ull n) {
    int first=0, last=l+1;
    int count = last-first;
    while (count>0) {
        int it = first, step=count/2; it+=step;
        
        ull p = pow2(a, it);
        if (p!=0 and pow2(a, it)<n) {
            first=++it;
            count-=step+1;
        } else count=step;
    }
    return first;
}

int main() {
	int t, a, l;
	ull n;
	cin >> t;
	while(cin >> a >> l >> n)
	{
	    ull link = 1+l;
        if (a>1) {
            int i=find(a, l, n)-1;
            link = (pow2(a, i+1)-1)/(a-1) + (l-i)*n;
        }
		cout << link * a * 4 << endl;
	}

	return 0;
}