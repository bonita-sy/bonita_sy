#include <stdio.h>
#include <stdlib.h>

int minof(const int a[], int n) {
	int i=1;
	int min = a[0];
	for(i; i<n; i++) {
		if (min > a[i])
			min = a[i];
	}
	return min;
}

int main(void) {
	int i;
	int *height;
	int people_number;

	printf("사람 수 : ");
	scanf("%d", &people_number);

	height = calloc(people_number, sizeof(int));
	puts("%d 사람의 키를 입력하세요.");
	for(i=0; i<people_number; i++) {
		printf("height[%d] : ", i);
		scanf("%d", &height[i]);
	}

	printf("최솟값은 %d입니다.\n", minof(height, people_number));
	free(height);
	
	return 0;
}
