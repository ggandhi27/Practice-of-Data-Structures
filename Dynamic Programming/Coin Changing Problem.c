#include <stdio.h>
#include <stdlib.h>

int count(int *arr,int m,int sum)
{
	if (sum==0)
	{
		return 1;
	}
	if (sum<0)
	{
		return 0;
	}
	if ((m<=0)&&(sum>=1))
	{
		return 0;
	}

	return count(arr,m-1,sum)+count(arr,m,sum-arr[m-1]);
}

int main()
{
	int n;
	int i;
	int *arr;
	int sum;
	int c;
	printf("Enter the number of different denominations : ");
	scanf("%d",&n);
	arr=(int *)malloc(n*sizeof(int));
	for(i=0;i<n;i++)
	{
		printf("Enter the first denomination : ");
		scanf("%d",&arr[i]);
	}
	printf("Enter the sum you want to have : ");
	scanf("%d",&sum);
	c=count(arr,n,sum);
	printf("The number of ways are : %d.",c);
	return 0;
}
