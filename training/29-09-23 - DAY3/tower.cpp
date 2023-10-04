#include<stdio.h>
int source(int a1,int a2,int a3)
{
	if(a2==0|a3==0)
	return 1;
}
int auxilary(int a2)
{
	
}
int main()
{
	int n,i;
	scanf("%d",&n);
	int s[n],a[n],d[n];
	for(i=0;i<n;i++)
	scanf("%d",&s[i]);
	for(i=0;i<n;i++)
	{
		if(source(s[i],a[i],d[i])|auxilary(s[i])|destination(s[i]))
		{
			
		}
	}
}
