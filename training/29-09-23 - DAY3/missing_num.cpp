//find the 1 missing number in an array
#include<stdio.h>
int main()
{
	/*int n,i;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	{
		if(a[i]!=i)
		{
			printf("Missing number:%d",i);
			break;
		}
	}*/
	int n,i;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	int x=0;
	for(i=0;i<=n;i++)
	x=x^i;
	for(i=0;i<n-1;i++)
	x=x^a[i];
	printf("Missing number: %d",x);	
}
