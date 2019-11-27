#include <stdio.h>
#include <stdlib.h>

int long_cmpr(const long *a, const long *b)
{
	if(*a < *b)
		return 1;
	else if (*a > *b)
		return -1;
	else
		return 0;
}

int main(void)
{
	int i, nx;
	long  ky, *x, *p;

	puts("bsearch 함수를 사용하여 검색");
	printf("요소 개수 : ");
	scanf("%d", &nx);
	x = calloc(nx, sizeof(long));
	printf("x[0] : ");
	scanf("%ld", &x[0]);
	for(i=1; i<nx; i++) {
		do {
			printf("x[%d] : ", i);
			scanf("%ld", &x[i]);
		} while(x[i] > x[i-1]);
	}

	printf("검색값 : ");
	scanf("%ld", &ky);
	p = bsearch(&ky, x, nx, sizeof(long), (long(*)(const void *, const void *))long_cmpr);

	if(p == NULL)
		puts("검색에 실패했습니다.");
	else
		printf("%ld는(은) x[%ld]에 있습니다.\n", ky, (long)(p-x));
	
	free(x);
	return 0;
}
