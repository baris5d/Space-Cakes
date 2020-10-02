#include <stdio.h>

int binsrch(int *a,int x,int low,int high){
	int mid;
	while(low<=high){
		mid=(low+high)/2;
		if(x<a[mid]) 
			high=mid-1;
		else if(x>a[mid])
			low=mid+1;
		else
			return mid;
	}
	return -1;	
}

int main(){
	
	int a[10]={1,4,15,122,240,260,350};
	
	int i=binsrch(a,122,0,6);
	printf("%d",i);
	
	return 0;
}
