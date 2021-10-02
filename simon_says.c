#include <stdio.h>

void printArray(int*, int);

int simonSays(int *, int *, int);

int main (){
	
	int a[2] = {1, 2};
	int b[2] = {5, 1};
	int c[2] = {1, 2};
	int d[2] = {5, 5};
	int e[5] = {1, 2, 3, 4, 5};
	int f[5] = {0, 1, 2, 3, 4};
	int g[5] = {1, 2, 3, 4, 5};
	int h[5] = {5, 5, 1, 2, 3};
	
	printf("%d ",simonSays(a, b, 2));
	printf("%d ",simonSays(c, d, 2));
	printf("%d ",simonSays(e, f, 5));
	printf("%d ",simonSays(g, h, 5));
	
	return 0;
}


void printArray(int *arr, int size){
	int i;
	for(i = 0; i < size; i++){
		printf("%d ", arr[i]);
	}
}


int simonSays(int *a, int *b, int size){
	int temp[size];
	int i;
	for(i = 0; i < size; i++){
		if(i == 0){
			temp[0] = 0;
		}else{
			temp[i] = a[i-1];
		}
	}
	
	for(i = 1; i < size; i++){
		if(temp[i] != b[i]){
			return 0;
		}
	}
	
	//printArray(temp, size);
	
	return 1;
}
