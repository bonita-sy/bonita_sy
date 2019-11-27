#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define swap(type, x, y) do { type t = x; x = y; y = t; } while(0)

void shuffle(int a[], int n) {
	int i=0; //index
	srand(time(NULL));
	for(i; i<n; i++) {
		int shf_index = rand() % n;
		swap(int, a[i], a[shf_index]);
	}
};

int main(void) {
	int i; //index
	int ary_length;
	int *org_ary;

	printf("배열의 길이를 입력하세요. : ");
	scanf("%d", &ary_length);
	org_ary = calloc(ary_length, sizeof(int));

	puts("배월 원소를 입력하세요.");
	for(i=0; i<ary_length; i++) {
		printf("원본 배열[%d] : ", i);
		scanf("%d", &org_ary[i]);
	}
	
	shuffle(org_ary, ary_length);

	for(i=0; i<ary_length; i++) {
		printf("셔플된 배열[%d] : %d\n", i, org_ary[i]);
	}
}
