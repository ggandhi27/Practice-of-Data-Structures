#include <stdio.h>
#include <stdlib.h>

int main()
{
	int t,n;
	int *arr;
	int i,count;
	scanf("%d",&t);
	while(t>0)
	{
		scanf("%d",&n);
		arr = (int *)malloc(n*sizeof(int));
		scanf("%d",&arr[0]);
		count = 1;
		for(i=1;i<n;i++)
		{
			scanf("%d",&arr[i]);
			if (arr[i]>arr[i-1])
			{
				arr[i]=arr[i-1]-1;
			}
			else
			{
				count++;
			}
		}
		printf("%d\n",count);
		t--;
	}
	return 0;
}
