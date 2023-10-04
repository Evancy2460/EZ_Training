#include<stdio.h>
int main()
{
	/*int n,i=0;
	scanf("%d",&n);
	while(1)
	{
		if(2<<i==n)
		{
			printf("yes");
			break;
		}
		if(2<<i>n)
		{
			printf("no");
			break;
		}
		i++;
	}*/
	int n,c=0;
	scanf("%d",&n);
	while(n)
	{
	   c++;
	   n=n&(n-1);
	}
	if(c==1)
	printf("true");
	else
	printf("false");

}


