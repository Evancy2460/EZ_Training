/*check ith bit is set or not(set means ith bit from right is 1 or not*/
#include<stdio.h>
main()
{
	int a,index,x;
	scanf("%d %d",&a,&index);
	x=(a&1<<(index-1));
	printf("%d",x);
}
