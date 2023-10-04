#include<stdio.h>
#include<math.h>
int main()
{
	int n,k;
	scanf("%d %d",&n,&k);
	int a=pow(2,k);
	printf("%d\n",a);
	if(n&(1<<(k))==0)
	printf("%d",n|a);
	else
	printf("%d",n^a);
	
}
