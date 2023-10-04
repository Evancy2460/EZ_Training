#include<stdio.h>
long long int fib(long long int n)
{
	if(n==0||n==1)
	return n;
	else
	return fib(n-1)+fib(n-2);
}
int main()
{
	long long int n,i;
	scanf("%lld",&n);
	for(i=0;i<n;i++)
	printf("%lld ",fib(i));
}
