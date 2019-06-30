#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<time.h>
int *cell, *start, *end, m, n;

void rando(int x, int y, double p)
{
	int i, j, thresh = p * RAND_MAX;
	
	m = x, n = y;
	end = start = realloc(start,((x+1)*(y+1)+1)* sizeof(int));

	memset(start, 0, (m + 1));
	cell = end = start + (m + 1);
	for (i =0; i < n; i++){
		for (j = 0; j < m; j++){
			*end++ = rand() < thresh ? 1 : -1 ;
	        }
		*end++ = 0;
	}

	end[-1] = 0;
	end -= ++m;

}

int ff(int *p)
{
	if (*p != 1 ) return 0;
	else{
             *p = 0;
	     if (p >= end ) return 1;
	     else return  ff(p-1) || ff(p+1) || ff(p+m) || ff(p-m);
	}

}

int percolate(void)
{
	int i; 
	for (i = 0; i < m && !ff(cell+i); i++);
	return i < m;

}

int main(void)
{
	FILE *fp1, *fp2, *fp3;
	int i, j, k, p, sum = 0, m = 0, rm;
	double pr;
	fp1 = fopen("perco.txt","w");
	fp2 = fopen("result.txt","w");
	fp3 = fopen("sum.txt","w");
	rm = 640;
	srand(time(NULL));
	for(p = 40; p < 50; p++){
		sum = 0;
		pr = p/100.0;
		for(k = 0; k < 25; k++){
			rando(rm, rm, pr);
			for(i = 0; i < rm; i++){
				for(j = 0; j < rm; j++){
					fprintf(fp1, "%f ", (float)(*cell/pr));	//start + m + 1
//					fprintf(fp1, "%d ", *cell);
					cell++;	
				}
//				fprintf(fp1, "\n");
			}
			cell = cell - rm * rm;
			m = percolate();
			fprintf(fp2, "%d ", m);
			sum += m;
			
//			cell = cell + m + m*n;
//			cell = cell + m - 1;
//			free(cell);
//			free(start);
//			free(end);
		}
		printf("%lf",pr);
		fprintf(fp3, "%d\n", sum);
	}
//	rando(40, 40, 0.6);
//	printf("\n%d",percolate());
	fclose(fp1);
	fclose(fp2);
	fclose(fp3);


	return 0;
}
