#include<stdio.h>
long long int fact(long long int n)
{
	if(n==0||n==1)
	return 1;
	else
	return n*fact(n-1);
}
int main()
{
	long long int n;
	scanf("%lld",&n);
	printf("%lld",fact(n));
}
