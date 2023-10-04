#include<stdio.h>
int main()
{
	int a=15,c=0;
	while(a)
	{
		c++;
		a=a&(a-1);
	}
	printf("%d",c);
/*	while(a>0)
	{
		if(a&1)
		{
			c++;
		}
		a=a>>1;
	}*/
}
