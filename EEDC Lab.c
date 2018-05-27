#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n,l,r,q,i,s;
	int *arr;
	scanf("%d",&n);
	s=0;
	arr = (int *)malloc(n * sizeof(int));
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
		s += arr[i];
	}
	scanf("%d",&q);
	for(i=0;i<q;i++)
	{
		scanf("%d %d",&l,&r);
		int j;
		int c;
		c=0;
		for(j=l;j<=r;j++)
		{
			int sum;
			sum = s-arr[j];
			if ((sum%2==0)&&(sum%3==0)&&(sum%5==0))
			{
				c++;
			}
		}
		printf("%d\n",c);
	}
	return 0;
}
