//https://edabit.com/challenge/43r7Ten6u2pE57mg2

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 

double stringToDouble(char *str){
	double d;
	sscanf(str, "%lf", &d);
	return d;
	
}

char freeThrows(char *str, int n){
	
	char *tempStr = malloc(sizeof(* str)-1);
	char c = 'x';
	int i = 0;
	double d, r;
	
	while(str[i] != '%'){
		i++;
	}
	
	strncpy(tempStr, str,i+2);
	
	printf("1o tempStr = %s\n", tempStr);
	
	d = stringToDouble(tempStr);
	
	r = pow(d/100, n)*100;
	
	snprintf(tempStr, 50, "%.0lf%%", r);
	
	printf("%s ", tempStr);
	
	return tempStr;
	
}


int main(){
	
	printf("%s",  freeThrows("75%", 5));
	
	return 0;
}



