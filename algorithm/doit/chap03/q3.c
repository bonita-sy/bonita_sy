#include <stdio.h>
#include <stdlib.h>

int search_idx(const int a[], int n, int key, int idx[]) {
	int i = 0;
	int j = 0;
	for(i; i<n; i++) {
		if(a[i] == key) {
			idx[j++] = i;
		}
	}
	return &idx;
}

int main(void) {
	int i, nx, ky, idx;
	int *x;
	int *y;
	puts("선형 검색");
	printf("요소 개수 : ");
	scanf("%d", &nx);
	x = calloc(nx, sizeof(int));
	for(i=0; i<nx; i++) {
		printf("x[%d] : ", i);
		scanf("%d", &x[i]);
	}
	printf("검색값 : ");
	scanf("%d", &ky);
	y = search_idx(x, nx, ky, y);
	printf("%d\n", sizeof(y)/sizeof(y[0]));
	free(x);
	return 0;
}
