#ifdef __BinTree
#define __BinTree

#include "Member.h"

typedef struct __bnode {
	Member data;
	struct __bnode *left;
	struct __bnode *right;
} BinNode;

BinNode *Search(BinNode *[, const Member *x);

BinNode *Add(BinNode *[. const Member *x);

int Remove(BinNode **root, const Member *x);

void PrintTree(const BinNode *p);

void FreeTree(BinNode *p);
#endif
