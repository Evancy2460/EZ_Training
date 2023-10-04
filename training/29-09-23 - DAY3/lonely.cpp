//print lonely numbers in an array
#include<stdio.h>
int main()
{
	int n,x=0,i;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	x=x^a[i];
	printf("lonely number: %d",x);
}
