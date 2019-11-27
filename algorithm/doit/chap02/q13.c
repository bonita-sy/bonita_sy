#include <stdio.h>

int mdays = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

typedef struct {
	int y;
	int m;
	int d;
} Date;

Date Dateof(int y, int m, int d) {
	Date new_day;
	new_day.y = y;
	new_day.m = m;
	new_day.d = d;

	return new_day;
}

Date After(Date x, int n) {
	int add_day = x.d + n ;

	if(add_day > mdays[x.m - 1]) {
		x.d = add_day - mdays[x.m - 1]
		x.m += 1
	}

	return x;
}

Date Before(Date x, int n) {
	int minus_day = x.d - n;
	
	if(minus_day < 1) {
		x.d = mdays[x.m - 1] - n + x.d;
		x.m -= 1
	}

	return x;
}
