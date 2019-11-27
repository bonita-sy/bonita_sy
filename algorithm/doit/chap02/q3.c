#include <stdio.h>
#include <stdlib.h>

double aveof(const int a[], int n) {
	int i=1; //index
	int sum = a[0];

	for(i; i<n; i++) {
		sum += a[i];
	}
	
	return (double)sum /(double) n; //int형 변수로 나누기 하면 소수점 잘림,,
}

int main(void) {
	int i=0; //index
	int *height; //calloc을 담을 포인터
	int people_number; //사람 수

	printf("사람 수 : ");
	scanf("%d", &people_number);

	height = calloc(people_number, sizeof(int));
	puts("%d 사람의 키를 입력하세요.");
	for(i=0; i<people_number; i++) {
		printf("height[%d] : ", i);
		scanf("%d", &height[i]);
	}

	printf("모든 키의 평균은 %f입니다.\n", aveof(height, people_number));
	free(height);
	
	return 0;
}
