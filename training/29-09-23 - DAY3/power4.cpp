#include<stdio.h>
int main()
{
	/*int n,i=0;
	scanf("%d",&n);
	if(n==1)
	printf("yes");
	else
	{
		while(1)
		{
			if(4<<(i*2)==n)
			{
				printf("yes");
				break;
			}
			if(4<<(i*2)>n)
			{
				printf("no");
				break;
			}
			i++;
		}
		
	}*/
	int n,c=0;
	scanf("%d",&n);
	while(n)
	{
	   c++;
	   n=n&(n-3);
	}
	if(c==1)
	printf("true");
	else
	printf("false");
}
