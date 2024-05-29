#include <stdio.h>

int main(){
    int array[100] = {16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14};
    for(int i = 0; i < 22; i++){
        printf("%c", array[i] + 64);
        if(i == 6){
            printf("{");
        }
    }
    printf("}");
    return 0;
}