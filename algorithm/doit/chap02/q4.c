#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int maxof(const int a[], int n) {
	int i;
	int max = a[0];
	for(i=1; i<n; i++) {
		if(a[i] > max) max = a[i];
	}
	return max;
}

int main(void) {
	int i;
	int *height;
	int number;
	srand(time(NULL));
	number = rand() % 16 + 5; //사람 수는 5이상 2-이하 난수로..

	height = calloc(number, sizeof(int));
	srand(time(NULL));
	for(i=0; i<number; i++) {
		height[i] = 100 + rand() % 90;
		printf("height[%d] = %d\n", i, height[i]);
	}

	printf("최댓값은 %d입니다.\n", maxof(height, number));
	free(height);

	return 0;
}
