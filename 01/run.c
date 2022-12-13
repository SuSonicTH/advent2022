#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 20
int main(int argc, char**argv){
    FILE *fp=fopen("input.txt","rt");
    if (fp==NULL){
        fprintf(stderr, "Could not open file input.txt");
        return 1;
    }

    long max = 0;
    long sum = 0;
    char line[MAX_LINE_LENGTH];
    
    while(fgets(line, MAX_LINE_LENGTH, fp)) {
        line[strlen(line)-1]=0;
        if (line[0] == 0){
            if (sum > max){
                max = sum;
            }
            sum = 0;
        } else {
            sum+=atol(line);
        }
    }
    fclose(fp);

    printf("max calories: %d\n", max);
    return 0;
}

