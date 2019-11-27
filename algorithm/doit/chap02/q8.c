#include <stdio.h>
#include <stdlib.h>

void ary_copy(int a[], const int b[], int n) {
	int i=0; //index
	for(i; i<n; i++) {
		a[i] = b[i];
		printf("원본 배열[%d]의 값 %d이 복사 배열[%d]에 복사되었습니다.\n", i, b[i], i);
	}
};

int main(void) {
	int i; //index
	int ary_length;
	int *org_ary; //복사될 배열
	int *copy_ary; //복사한 배열

	printf("배열의 길이를 입력하세요. : ");
	scanf("%d", &ary_length);
	org_ary = calloc(ary_length, sizeof(int));
	copy_ary = calloc(ary_length, sizeof(int));

	puts("배월 원소를 입력하세요.");
	for(i=0; i<ary_length; i++) {
		printf("원본 배열[%d] : ", i);
		scanf("%d", &org_ary[i]);
	}
	
	ary_copy(copy_ary, org_ary, ary_length);

	for(i=0; i<ary_length; i++) {
		printf("복사 배열[%d] : %d\n", i, copy_ary[i]);
	}
}
